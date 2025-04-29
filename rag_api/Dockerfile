FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir \
    fastapi uvicorn[standard] \
    langchain langchain-community \ 
    langchain-ollama \
    chromadb langchain-chroma

CMD ["uvicorn", "app-stream:app", "--host", "0.0.0.0", "--port", "8000"]