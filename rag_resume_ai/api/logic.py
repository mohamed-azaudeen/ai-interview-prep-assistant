import re
from rag_resume_ai.app.qa_chain import get_qa_chain

print("🔄 Loading RAG pipeline...")
qa_chain = get_qa_chain()
print("✅ RAG pipeline ready")

def ask_resume_logic(question: str):
    return qa_chain.invoke(question)

def match_resume_jd_logic(resume_text: str, jd_text: str):
    prompt = f"""
    Compare the following resume and job description.
    Resume: {resume_text}
    Job Description: {jd_text}
    STRICTLY return output in the following format:
    Match Score: <number between 0-100>
    Matched Skills:
    - skill1
    Missing Skills:
    - skill1
    Summary: <short summary>
    """
    raw_response = qa_chain.invoke(prompt)
    
    score_match = re.search(r"Match Score:\s*(\d+)", raw_response)
    match_score = int(score_match.group(1)) if score_match else 0

    def extract_list(section):
        pattern = rf"{section}:\s*((?:- .*\n?)*)"
        match = re.search(pattern, raw_response)
        return [i.replace("- ", "").strip() for i in match.group(1).split("\n") if i.strip()] if match else []

    summary_match = re.search(r"Summary:\s*(.*)", raw_response, re.DOTALL)
    summary = summary_match.group(1).strip() if summary_match else raw_response

    return {
        "match_score": match_score,
        "matched_skills": extract_list("Matched Skills"),
        "missing_skills": extract_list("Missing Skills"),
        "summary": summary
    }

def generate_interview_questions_logic(resume_text, jd_text, question_type):
    prompt = f"""You are a senior technical recruiter. Generate 5 questions.
    Focus: {question_type} | Resume: {resume_text} | JD: {jd_text}"""
    return qa_chain.invoke(prompt)