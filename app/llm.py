from langchain_ollama import ChatOllama


def get_llm():
    """
    Initialize local LLaMA model via Ollama
    """
    return ChatOllama(
        model="llama3",
        temperature=0
    )
