import streamlit as st
import requests
from PyPDF2 import PdfReader


def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


API_BASE = "http://127.0.0.1:8000"


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
    st.subheader("📊 Resume vs Job Description Match")

    if st.button("🔍 Analyze Resume Match", use_container_width=True):
        if not uploaded_resume or not jd_text:
            st.warning("Please upload a resume and paste a Job Description.")
        else:
            resume_text = extract_text_from_pdf(uploaded_resume)

            with st.spinner("Running ATS analysis..."):
                response = requests.post(
                    f"{API_BASE}/match_resume_jd",
                    json={
                        "resume_text": resume_text,
                        "jd_text": jd_text
                    }
                )

            if response.status_code == 200:
                data = response.json()

                col1, col2, col3 = st.columns(3)
                col1.metric("🎯 Match Score", f"{data['match_score']}%")
                col2.metric("✅ Matched Skills", len(data["matched_skills"]))
                col3.metric("❌ Missing Skills", len(data["missing_skills"]))

                st.divider()

                st.subheader("✅ Matched Skills")
                st.write(data["matched_skills"])

                st.subheader("❌ Missing Skills")
                st.write(data["missing_skills"])

                st.subheader("📝 ATS Summary")
                st.info(data["summary"])

            else:
                st.error("Failed to analyze resume. Is FastAPI running?")


with tab2:
    st.subheader("🎤 Interview Preparation")

    question_type = st.selectbox(
        "Choose Interview Focus Area",
        [
            "Resume-based",
            "JD-based",
            "Skill-gap focused",
            "GenAI / ML concepts",
            "Behavioral (HR)"
        ]
    )

    if st.button("🧠 Generate Interview Questions", use_container_width=True):
        if not uploaded_resume or not jd_text:
            st.warning("Please upload a resume and paste a Job Description.")
        else:
            resume_text = extract_text_from_pdf(uploaded_resume)

            with st.spinner("Preparing personalized interview questions..."):
                response = requests.post(
                    f"{API_BASE}/interview_questions",
                    json={
                        "resume_text": resume_text,
                        "jd_text": jd_text,
                        "question_type": question_type
                    }
                )

            if response.status_code == 200:
                st.subheader("📋 Likely Interview Questions")
                st.write(response.json()["questions"])
            else:
                st.error("Could not generate interview questions.")


with tab3:
    st.subheader("💬 Ask Questions About Your Resume")

    user_query = st.text_input(
        "Ask anything (skills, experience, gaps, improvements)"
    )

    if st.button("Ask AI", use_container_width=True):
        if not user_query:
            st.warning("Please enter a question.")
        else:
            with st.spinner("Thinking..."):
                response = requests.post(
                    f"{API_BASE}/ask",
                    json={"question": user_query}
                )

            if response.status_code == 200:
                st.success(response.json()["answer"])
            else:
                st.error("Failed to get response from AI.")
