import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

def get_llm():
    """
    Returns Gemini if GOOGLE_API_KEY is present,
    otherwise falls back to local ollama.
    """

    google_api_key = os.getenv("GOOGLE_API_KEY")
    
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=google_api_key,
        temperature=0
    )

