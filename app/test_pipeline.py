import os
from .ingestion import ingest_all_documents
from .embeddings import get_embeddings
from .vectorstore import create_and_save_faiss_index
from .qa_chain import get_qa_chain

def main():
    base_path = r"C:\Users\azaru\Azar documents\Data Science Projects\Gen AI Projects\RAG_Model"
    index_path = "faiss_index"
    
    print("--- Phase 1: Ingesting Documents ---")
    chunks = ingest_all_documents(base_path)
    print(f"Total chunks created: {len(chunks)}")

    print("\n--- Phase 2: Generating Embeddings & Vector Store ---")
    embeddings = get_embeddings()
    
    vector_db = create_and_save_faiss_index(
        documents=chunks, 
        embeddings=embeddings, 
        index_path=index_path
    )
    print(f"Vector store saved at: {index_path}")

    print("\n--- Phase 3: Initializing RAG Chain ---")
    qa_chain = get_qa_chain()

    print("\n--- Phase 4: Querying ---")
    query = "What are my strongest GenAI projects?"
    
    try:
        response = qa_chain.invoke(query)
        print("\n=== AI CAREER ASSISTANT RESPONSE ===\n")
        print(response)
    except Exception as e:
        print(f"An error occurred during invocation: {e}")

if __name__ == "__main__":
    main()