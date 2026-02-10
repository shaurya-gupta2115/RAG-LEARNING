# RAG Learning Pipeline 🚀

A simple, modular RAG (Retrieval-Augmented Generation) system built to understand how to bridge the gap between local documents and LLMs. It handles everything from loading various file types to querying them using Groq's Llama 3 models.

## What's inside?
- **Data Ingestion:** Loads PDFs, TXT files, and more (using LangChain loaders).
- **Vector Store:** Uses FAISS for fast local similarity search.
- **Embeddings:** `all-MiniLM-L6-v2` via Sentence Transformers.
- **LLM Integration:** Powered by Groq (currently using `llama-3.3-70b-versatile` for speed and quality).
- **Interactive CLI:** A simple terminal loop to ask questions about your data.

## Quick Start

### 1. Prerequisites
I'm using `uv` for package management because it's way faster than pip. If you don't have it:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Set up your .env
You'll need a Groq API key. Create a `.env` file in the root:
```env
GROQ_API_KEY=your_key_here
```

### 3. Run it
Just drop your documents into the `data/` folder and run:
```bash
uv run python main.py
```
The first time you run it, it'll chunk your documents and build the FAISS index. After that, it'll just load the saved index from `faiss_store/`.

## Project Structure
- `src/data_loader.py` - Logic for reading different file formats.
- `src/embedding.py` - Document splitting and vector generation.
- `src/vectorstore.py` - FAISS management (save/load/query).
- `src/search.py` - The "brain" that pulls context and sends prompts to Groq.
- `main.py` - The CLI entry point.

## A few notes / "Gotchas"
- **Model Choice:** I originally had this set to `gemma2-9b-it`, but Groq decommissioned it. Switched to `llama-3.3-70b-versatile`.
- **Imports:** Make sure you're running from the root so the `src.` imports resolve correctly.
- **FAISS:** If you update your documents in `data/`, you might need to delete the `faiss_store/` folder to force a rebuild.

## To-Do
- [ ] Add support for CSV and Excel.
- [ ] Improve chunking strategies for better context.
- [ ] Maybe add a simple Streamlit UI later?
