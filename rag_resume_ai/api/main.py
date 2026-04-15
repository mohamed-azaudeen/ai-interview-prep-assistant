from fastapi import FastAPI
from pydantic import BaseModel
import re

from rag_resume_ai.app.qa_chain import get_qa_chain

app = FastAPI(
    title="GenAI Resume RAG API",
    description="Offline RAG system using LLaMA + FAISS",
    version="1.0.0"
)

print("🔄 Loading RAG pipeline...")
qa_chain = get_qa_chain()
print("✅ RAG pipeline ready")

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
    """
    Ask Questions using resume + indexed documents

    """
    response = qa_chain.invoke(payload.question)
    return {"answer": response}

@app.post("/match_jd")
def match_job_description(payload: JDMatchRequest):
    """
    Compare resume against a Job Description
    
    """
    query = f"""
    Compare my resume with the following Job Description.
    Identify:
    - Missing skills
    - Matching skills
    - Overall suitability

    Job Description:
    {payload.job_description}
   
    """

    response = qa_chain.invoke(query)
    return {"analysis": response} 

@app.post("/match_resume_jd")
def match_resume_jd(payload: ResumeJDMatchRequest):
    prompt = f"""
    Compare the following resume and job description.

    Resume:
    {payload.resume_text}

    Job Description:
    {payload.jd_text}

    STRICTLY return output in the following format:

    Match Score: <number between 0-100>

    Matched Skills:
    - skill1
    - skill2

    Missing Skills:
    - skill1
    - skill2

    Summary:
    <short professional summary>
    """

    raw_response = qa_chain.invoke(prompt)
    score_match = re.search(r"Match Score:\s*(\d+)", raw_response)
    match_score = int(score_match.group(1)) if score_match else 0

    def extract_list(section):
        pattern = rf"{section}:\s*((?:- .*\n?)*)"
        match = re.search(pattern, raw_response)
        if not match:
            return []
        return [i.replace("- ", "").strip() for i in match.group(1).split("\n") if i.strip()]

    matched_skills = extract_list("Matched Skills")
    missing_skills = extract_list("Missing Skills")

    summary_match = re.search(r"Summary:\s*(.*)", raw_response, re.DOTALL)
    summary = summary_match.group(1).strip() if summary_match else raw_response

    return {
        "match_score": match_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "summary": summary
    }

@app.post("/interview_questions")
def interview_questions(payload: InterviewQuestionRequest):
    prompt = f"""
    You are a senior technical recruiter.

    Based on the resume and job description,
    generate 5 realistic interview questions.

    Focus Type: {payload.question_type}

    Resume:
    {payload.resume_text}

    Job Description:
    {payload.jd_text}
    """

    response = qa_chain.invoke(prompt)

    return {"questions": response}
