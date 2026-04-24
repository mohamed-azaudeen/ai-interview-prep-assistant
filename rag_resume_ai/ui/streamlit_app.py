import streamlit as st
from PyPDF2 import PdfReader
from rag_resume_ai.api.logic import ask_resume_logic, match_resume_jd_logic, generate_interview_questions_logic
import time
import google.api_core.exceptions

def call_with_retry(func, *args, max_retries=3, delay=2, **kwargs):
    """Retries a function call if a 503 error occurs."""
    for i in range(max_retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if "503" in str(e) or "high demand" in str(e).lower():
                if i < max_retries - 1:
                    st.warning(f"Gemini is busy. Retrying in {delay}s... (Attempt {i+1}/{max_retries})")
                    time.sleep(delay)
                    delay *= 2 
                    continue

            st.error(f"An error occurred: {e}")
            return None
        

def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

st.set_page_config(
    page_title="AI Resume Intelligence",
    layout="wide",
    page_icon="🤖"
)

st.title("🤖 AI Resume Intelligence Platform")
st.caption("Personalized Resume Checker • ATS Matcher • Interview Prep AI")

st.divider()


uploaded_resume = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)

jd_text = st.text_area(
    "📌 Paste Job Description",
    height=220
)


tab1, tab2, tab3 = st.tabs(
    ["📊 ATS Match", "🎤 Interview Prep", "💬 Ask Resume"]
)

with tab1:
    if st.button("🔍 Analyze Resume Match"):
        if uploaded_resume and jd_text:
            resume_text = extract_text_from_pdf(uploaded_resume)
            with st.spinner("Analyzing..."):
                data = call_with_retry(match_resume_jd_logic, resume_text, jd_text)
                if data: 
                    st.metric("🎯 Match Score", f"{data['match_score']}%")
                    st.subheader("✅ Matched Skills")
                    st.write(data["matched_skills"])
                    st.info(data["summary"])

with tab2:
    q_type = st.selectbox("Focus Area", ["Resume-based", "Skill-gap focused"])
    if st.button("🧠 Generate Questions"):
        if uploaded_resume:
            resume_text = extract_text_from_pdf(uploaded_resume)
            with st.spinner("Generating..."):
                questions = call_with_retry(generate_interview_questions_logic, resume_text, jd_text, q_type)
                if questions:
                    st.write(questions)
        else:
            st.warning("Please upload a resume first.")

with tab3:
    query = st.text_input("Ask AI about resume")
    if st.button("Ask"):
        answer = ask_resume_logic(query)
        st.success(answer)