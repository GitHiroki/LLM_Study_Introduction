# LangChain × Ollama で学ぶ LLM & RAG 超入門

このリポジトリは、勉強会「LangChain × Ollamaで学ぶLLM & RAG超入門」で使用する教材です。  
参加者は本リポジトリを clone して、ローカル環境で RAG システムを体験できます。

> 💡 push は不要です。ローカルで完結します。

## 内容概要

完全ローカル環境で以下を構築します：

- 日本語対応 LLM（Gemma3）と日本語埋め込みモデル（Ruri-base）による質問応答
- LangChain + FastAPI による RAG 構成
- OpenAI API 互換のエンドポイント（`/v1/chat/completions`）
- Open WebUI をフロントエンドに使った対話体験

## 推奨環境

| 項目       | 内容                                     |
|------------|------------------------------------------|
| OS         | WSL2 (Ubuntu 22.04) + Windows 11         |
| Docker     | Docker Desktop（WSL バックエンド）       |
| GPU        | CUDA 12 以上 / VRAM 8GB+（任意、CPU可）  |
| ポート     | 11434, 8000, 3000 を使用                 |

## セットアップ手順

1. リポジトリを clone  
   ```bash
   git clone https://github.com/your-org/llm-rag-intro.git
   cd llm-rag-intro
   ```

2. Docker コンテナを起動  
   ```bash
   docker compose up -d
   ```

3. モデルを取得（別ターミナルで実行）  
   ```bash
   docker exec -it ollama ollama pull gemma3:1b
   docker exec -it ollama ollama pull kun432/cl-nagoya-ruri-base
   ```

4. Open WebUI にアクセス  
   - http://localhost:3000  
   - モデル選択で `gemma-rag` を選択 → 質問を入力


## 参考

- 勉強会スライド: [LangChain × Ollamaで学ぶLLM & RAG超入門](https://speakerdeck.com/dassimen001/langchain-x-ollamadexue-bullm-and-ragchao-ru-men)
- LangChain: https://www.langchain.com/
- Ollama: https://ollama.com/
- Open WebUI: https://github.com/open-webui/open-webui

---

## ❗ 注意

- 本リポジトリは読み取り専用です。変更を加えたい場合はローカルで fork またはコピーしてください。
- `docs/` フォルダに独自ファイルを追加して、RAGを自由に試せます。
