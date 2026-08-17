# RAG Project

A Retrieval-Augmented Generation (RAG) system that answers questions over a custom document corpus, combining semantic search with an LLM to generate grounded, source-cited answers.

## Status: Work in Progress

## Overview

<!-- Replace this with a couple of sentences on your actual corpus: what documents, what domain, why this use case -->
This project builds a searchable knowledge base from `Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, Attention Is All You Need, An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale and Retrieval-Augmented Generation for Large Language Models: A Survey` and will let users ask natural-language questions and get answers grounded in that corpus, with citations back to the source.

## What's done so far

- Document loading (`DirectoryLoader` / `PyPDFLoader`)
- Chunking with `RecursiveCharacterTextSplitter` (chunk_size=500, overlap=50)
- Embedding generation with `sentence-transformers` (`all-MiniLM-L6-v2`)
- Vector store indexing (Chroma/FAISS), persisted to disk
- Retrieval sanity-checked with `similarity_search` on sample queries

## What's next (roadmap)

- Connect the retriever into a full LangChain pipeline (retriever → prompt with context → LLM) using LCEL
- LLM integration with answers that cite the source chunk
- Advanced retrieval: re-ranking (cross-encoder) and hybrid search (embeddings + BM25)
- Evaluation set + metrics (RAGAS or a custom rubric)
- Interactive UI (Streamlit or Gradio)

## Tech stack

- Python 3.11
- [LangChain](https://python.langchain.com/) / `langchain-community`
- [sentence-transformers](https://www.sbert.net/)
- ChromaDB (or FAISS)

## Project structure

```
rag-project/
├── data/                          # source documents (raw corpus)
├── src/
│   └── 01_retrieval_tests.ipynb   # similarity_search sanity checks
│   └── rag_vectorstore_retrieval.ipynb 
├── requirements.txt
└── README.md
```
## Setup

```bash
conda activate py311ml
pip install -r requirements.txt
```

## Usage (so far)

```bash
python src/ingest.py   # builds and persists the vector index
```

Then open `notebooks/01_retrieval_tests.ipynb` to run retrieval queries against the index.

## License

<!-- MIT is a common default for portfolio projects -->
MIT
