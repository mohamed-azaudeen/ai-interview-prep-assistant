# 🤖 AI Resume & JD Assistant (RAG-Based)

An end-to-end **Retrieval-Augmented Generation (RAG)** system that:
- Matches resumes with job descriptions (ATS-style scoring)
- Identifies skill gaps
- Generates interview questions
- Provides resume-aware Q&A
- Works fully offline using FAISS + LLaMA

---

## 🚀 Features

✅ Resume ↔ Job Description matching with score (%)  
✅ Matched & missing skills extraction  
✅ Resume-based question answering  
✅ Interview question generator (JD + Resume aware)  
✅ FastAPI backend + Streamlit frontend  
✅ Offline RAG (FAISS vector store)

---

## 🧠 System Architecture

Resume / JD (PDF/Text)
↓
Text Chunking
↓
Embedding (Sentence Transformers)
↓
FAISS Vector Store
↓
Retriever
↓
LLM (LLaMA)
↓
FastAPI (REST API)
↓
Streamlit UI


---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **FAISS**
- **FastAPI**
- **Streamlit**
- **Sentence Transformers**
- **LLaMA / Open-source LLM**

---

## 📂 Project Structure

rag_resume_ai/
├── app/ # Core RAG logic
├── api/ # FastAPI backend
├── ui/ # Streamlit frontend
├── data/ # Sample resumes & JDs


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/rag-resume-ai.git
cd rag-resume-ai

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Running the Application

🔹 Start FastAPI Backend
uvicorn rag_resume_ai.api.main:app --reload

Visit:
API Docs → http://127.0.0.1:8000/docs

🔹 Start Streamlit UI
streamlit run rag_resume_ai/ui/streamlit_app.py

Visit:
UI → http://localhost:8501"# ai-interview-prep-assistant" 

