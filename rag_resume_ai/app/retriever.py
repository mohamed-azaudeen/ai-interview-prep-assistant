from langchain_community.vectorstores import FAISS
from rag_resume_ai.app.embeddings import get_embeddings
import os

def load_retriever():
    index_path = "faiss_index"
    k = 3

    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    full_index_path = os.path.join(base_dir, index_path)

    if not os.path.exists(full_index_path):
        print(f"🚀 Index not found at {full_index_path}. Please ensure it is uploaded.")
        return None
    
    """
    Load FAISS index and return a retriever
    """
    embeddings = get_embeddings()

    vector_db = FAISS.load_local(
        full_index_path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_db.as_retriever(
        search_kwargs={"k": k}
    )
