from app.ingestion.loader import load_document
from app.ingestion.chunker import chunk_text
from app.ingestion.embedder import Embedder
from app.ingestion.vector_store import VectorStore
from app.llm import LLM


def main():
    print("Enterprise Document Intelligence System initialized")

    # Load and process document
    text = load_document("data/sample.pdf")
    chunks = chunk_text(text)
    print(f"\nTotal chunks: {len(chunks)}")

    # Embeddings
    embedder = Embedder()
    embeddings = embedder.embed(chunks)

    # Vector store
    vector_store = VectorStore(embeddings, chunks)

    # User question
    question = "What is Arfa's professional background?"

    # Retrieve relevant chunks
    query_embedding = embedder.embed([question])[0]
    results = vector_store.search(query_embedding, top_k=3)

    # Combine context
    context = "\n\n".join([r["text"] for r in results])

    # LLM answer
    llm = LLM()
    answer = llm.answer(question, context)

    print("\nFinal Answer:\n")
    print(answer)


if __name__ == "__main__":
    main()
