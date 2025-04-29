from fastapi import FastAPI
from pydantic import BaseModel
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
import os, uuid, time

OLLAMA = os.getenv("OLLAMA_BASE_URL")
CHROMA_DIR = os.getenv("CHROMA_DIR", "./chroma_store")

# 文書ロード & ベクトル化
# docs   = TextLoader("docs/*.md").load()
loader = DirectoryLoader("docs", glob="**/*.md", loader_cls=TextLoader)
docs   = loader.load()

splits = RecursiveCharacterTextSplitter(
            chunk_size=400, chunk_overlap=40).split_documents(docs)

emb = OllamaEmbeddings(
        model="kun432/cl-nagoya-ruri-base",
        base_url=OLLAMA)

store = Chroma.from_documents(
          splits, emb,
          persist_directory=CHROMA_DIR,
          collection_name="my_docs")
store.persist()

retriever = store.as_retriever(k=3)
llm = ChatOllama(model="gemma3:1b",
                 base_url=OLLAMA,
                 temperature=0.2)

qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever)

# OpenAI 互換エンドポイント
class Msg(BaseModel):
    role: str
    content: str

class ChatReq(BaseModel):
    model: str
    messages: list[Msg]

app = FastAPI()

@app.get("/v1/models")
def list_models():
    return {
        "object": "list",
        "data": [
            {"id": "gemma-rag", "object": "model", "owned_by": "local"}
        ]
    }

@app.post("/v1/chat/completions")
def completions(req: ChatReq):
    prompt = req.messages[-1].content
    answer = qa_chain.run(prompt)
    return {
        "id": f"chatcmpl-{uuid.uuid4()}",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": "gemma-rag",
        "choices": [{
            "index": 0,
            "message": {"role": "assistant", "content": answer},
            "finish_reason": "stop"
        }]
    }