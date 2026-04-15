from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from .retriever import load_retriever
from .llm import get_llm


def get_qa_chain():
    """
    Build Retrieval-Augmented Generation (RAG) chain
    """

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are an AI Career Assistant.

Use context from resumes, job descriptions,
company roles, and interview questions.

Answer professionally, precisely, and clearly.

Context:
{context}

Question:
{question}

Answer:
"""
    )

    llm = get_llm()
    retriever = load_retriever()

    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain
