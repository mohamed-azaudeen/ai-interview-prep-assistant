import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

base_path=r"C:\Users\azaru\Azar documents\Data Science Projects\Gen AI Projects\RAG_Model"

def load_documents(folder_path: str, doc_type: str):
    documents = []

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if file.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        elif file.endswith(".txt"):
            loader = TextLoader(file_path)
        else:
            continue

        loaded_docs = loader.load()

        for doc in loaded_docs:
            doc.metadata["source_type"] = doc_type
            doc.metadata["file_name"] = file

        documents.extend(loaded_docs)

    return documents


def ingest_all_documents(base_path: str):
    all_docs = []

    sources = {
        "resume": "resume",
        "job_descriptions": "job_description",
        "company_roles": "company_role",
        "interview_questions": "interview_question",
    }

    for folder, doc_type in sources.items():
        folder_path = os.path.join(base_path, folder)
        if os.path.exists(folder_path):
            all_docs.extend(load_documents(folder_path, doc_type))

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(all_docs)
    return chunks
