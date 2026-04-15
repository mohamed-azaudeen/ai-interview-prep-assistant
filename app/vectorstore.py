import os
from langchain_community.vectorstores import FAISS
from langchain.embeddings.base import Embeddings


def create_and_save_faiss_index(
    documents,
    embeddings: Embeddings,
    index_path: str = "faiss_index"
):
    """
    Create FAISS vector store from documents and save to disk
    """
    vector_db = FAISS.from_documents(
        documents=documents,
        embedding=embeddings
    )

    vector_db.save_local(index_path)
    return vector_db


def load_faiss_index(
    embeddings: Embeddings,
    index_path: str = "faiss_index"
):
    """
    Load existing FAISS vector store from disk
    """
    if not os.path.exists(index_path):
        raise FileNotFoundError(f"FAISS index not found at {index_path}")

    vector_db = FAISS.load_local(
        index_path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_db


def similarity_search(
    vector_db: FAISS,
    query: str,
    k: int = 3
):
    """
    Perform similarity search on FAISS index
    """
    return vector_db.similarity_search(query, k=k)
