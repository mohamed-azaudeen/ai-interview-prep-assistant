import streamlit as st
from PyPDF2 import PdfReader
from rag_resume_ai.api.logic import ask_resume_logic, match_resume_jd_logic, generate_interview_questions_logic


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
                # Calling logic directly
                data = match_resume_jd_logic(resume_text, jd_text)
                st.metric("🎯 Match Score", f"{data['match_score']}%")
                st.subheader("✅ Matched Skills")
                st.write(data["matched_skills"])
                st.info(data["summary"])

with tab2:
    q_type = st.selectbox("Focus Area", ["Resume-based", "Skill-gap focused"])
    if st.button("🧠 Generate Questions"):
        resume_text = extract_text_from_pdf(uploaded_resume)
        questions = generate_interview_questions_logic(resume_text, jd_text, q_type)
        st.write(questions)

with tab3:
    query = st.text_input("Ask AI about resume")
    if st.button("Ask"):
        answer = ask_resume_logic(query)
        st.success(answer)