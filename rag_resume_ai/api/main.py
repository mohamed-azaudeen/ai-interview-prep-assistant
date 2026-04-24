from fastapi import FastAPI
from pydantic import BaseModel
from rag_resume_ai.api.logic import ask_resume_logic, match_resume_jd_logic, generate_interview_questions_logic

app = FastAPI(
    title="GenAI Resume RAG API",
    description="Offline RAG system using LLaMA + FAISS"
)


class AskRequest(BaseModel):
    question: str

class JDMatchRequest(BaseModel):
    job_description: str

class ResumeJDMatchRequest(BaseModel):
    resume_text: str
    jd_text: str

class InterviewQuestionRequest(BaseModel):
    resume_text: str
    jd_text: str
    question_type: str


@app.get("/")
def root():
    return {
        "message": "RAG Resume Assistant API is running",
        "endpoints": ["/ask", "/match_jd", "/health","/match_resume_jd","/interview_questions"]
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "llm": "llama3",
        "vector_store": "faiss",
        "rag": "active"
    }

@app.post("/ask")
def ask_questions(payload: AskRequest):
    return {"answer": ask_resume_logic(payload.question)}

@app.post("/match_resume_jd")
def match_resume(payload: ResumeJDMatchRequest):
    return match_resume_jd_logic(payload.resume_text, payload.jd_text)

@app.post("/interview_questions")
def interview_questions(payload: InterviewQuestionRequest):
    return {"questions": generate_interview_questions_logic(payload.resume_text, payload.jd_text, payload.question_type)}