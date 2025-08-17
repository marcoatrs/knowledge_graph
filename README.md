# Knowledge Graph + Semantic Search + Chat

This project is an experimental Python system that combines:

- **Document ingestion** (PDF, TXT, DOCX in the future).
- **Semantic search** using embeddings.
- **Knowledge Graph** for entity-relation queries.
- **Hybrid search engine** that mixes both approaches.
- **Chat interface** with LLMs (RAG style).

## 🚀 Project Structure
- `src/`: Core modules (data loading, embeddings, knowledge graph, hybrid engine, chatbot).
- `main.py`: CLI interface using `curses` for a chat-like experience.
- `data/`: Sample documents for testing.
- `tests/`: Unit tests.

## 🛠 Installation
```bash
git clone https://github.com/marcoatrs/knowledge_graph.git
cd knowledge_chat
uv venv
uv sync
