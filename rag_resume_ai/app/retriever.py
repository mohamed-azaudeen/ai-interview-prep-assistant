from langchain_community.vectorstores import FAISS
from rag_resume_ai.app.embeddings import get_embeddings


def load_retriever(
    index_path: str = "faiss_index",
    k: int = 3
):
    """
    Load FAISS index and return a retriever
    """
    embeddings = get_embeddings()

    vector_db = FAISS.load_local(
        index_path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_db.as_retriever(
        search_kwargs={"k": k}
    )
