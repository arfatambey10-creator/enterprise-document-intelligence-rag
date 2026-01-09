Enterprise Document Intelligence System (RAG)

A production-style Enterprise Document Intelligence system built in Python using Retrieval-Augmented Generation (RAG) principles.

This project focuses on system design, retrieval quality, and practical AI engineering trade-offs, rather than model-specific performance or paid APIs.

It demonstrates how unstructured documents (PDFs) can be ingested, indexed, and queried reliably in a production-like environment.

🎯 Project Goals

Build a clean, modular RAG pipeline suitable for enterprise use cases

Emphasise retrieval quality over raw model output

Design for cost, latency, and extensibility

Demonstrate applied AI engineering, not research prototypes

🧠 System Overview

The system follows a standard document intelligence pipeline:

Document Ingestion

PDF text extraction

Basic preprocessing and cleaning

Chunking Strategy

Overlapping text chunks to preserve context

Configurable chunk size and overlap

Embedding & Vector Storage

Text chunks converted to vector representations

Stored in an in-memory vector store for fast similarity search

Retrieval

Query embedding

Cosine similarity to retrieve the most relevant document chunks

Response Generation (Mocked)

Retrieved context passed to a mock LLM interface

Designed to be easily replaceable with real LLMs (OpenAI, Ollama, etc.)

🏗️ Project Structure
app/
├── ingestion/
│   ├── loader.py        # PDF loading and text extraction
│   ├── chunker.py       # Text chunking logic
│   ├── embedder.py      # Embedding generation
│   └── vector_store.py  # Vector storage and similarity search
│
├── llm.py               # Mock LLM interface
└── main.py              # End-to-end pipeline execution


This modular structure mirrors how production systems are typically organised, making individual components easy to test, replace, or extend.

📊 Evaluation & Engineering Considerations

Rather than focusing only on “correct answers”, this project evaluates the system from an engineering perspective:

Retrieval Quality

Relevance of retrieved chunks to the query

Impact of chunk size and overlap on results

Latency Awareness

Clear separation of ingestion, retrieval, and generation stages

Designed to measure and optimise response time per stage

Reliability

Mock LLM ensures responses are grounded only in retrieved context

Helps detect retrieval issues without relying on paid APIs

This approach reflects how applied AI systems are assessed in real product teams.

🔒 Design Decisions

No paid APIs used
To keep the system reproducible and cost-free, external LLMs are mocked.

Mock LLM instead of live models
Allows full pipeline testing, evaluation, and iteration without infrastructure dependencies.

Evaluation-first mindset
Retrieval quality is treated as a first-class concern, not an afterthought.

All major trade-offs are intentional and documented.

🚧 Limitations

No live LLM integration (by design)

In-memory vector store (suitable for prototyping, not large-scale deployment)

Basic evaluation metrics (designed to be extended)

These limitations reflect realistic constraints and are explicitly acknowledged.

🔮 Future Improvements

Plug-in support for OpenAI / Ollama / local LLMs

Persistent vector databases (FAISS, Chroma, etc.)

Automated evaluation and regression testing

CI-based performance monitoring

🧩 Why This Project Matters

This project demonstrates:

Practical Python engineering

Understanding of RAG system design

Awareness of production trade-offs

Ability to build and reason about applied AI systems

It is intended as a foundation for real-world document intelligence applications.

📌 Author

Arfa Tambey
Applied AI & Python Engineering
GitHub: https://github.com/arfatambey10-creator