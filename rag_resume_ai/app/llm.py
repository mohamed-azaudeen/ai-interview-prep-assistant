import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
load_dotenv()

def get_llm():
    """
    Returns Gemini if GOOGLE_API_KEY is present,
    otherwise falls back to local ollama.
    """

    google_api_key = os.getenv("GOOGLE_API_KEY")
    
    if google_api_key:
        return ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=google_api_key,
            temperature=0
        )
    else:
        return ChatOllama(
            model="llama3",
            temperature=0,
            base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        )
