---
title: AI Resume Intelligence
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 8501
pinned: false
---

# 🤖 AI Resume Intelligence Platform (MLOps & RAG)

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Docker Support](https://img.shields.io/badge/Docker-Supported-blue.svg?logo=docker)](Dockerfile)
[![Hugging Face Space](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-yellow)](https://huggingface.co/spaces/Azar-Mhmd/ai-resume-intelligence)

An end-to-end **Generative AI & MLOps** project featuring a RAG (Retrieval-Augmented Generation) system. This platform automates ATS scoring, skill-gap analysis, and personalized interview preparation using open-source LLMs.

## 🚀 Key Features

- **🎯 ATS Matcher:** Advanced semantic comparison between Resume (PDF) and Job Descriptions.
- **🔍 Skill Analytics:** Automated extraction of matched and missing technical skills.
- **🎤 Interview Coach:** Generates contextual interview questions based on specific job-role requirements and candidate experience.
- **💬 Resume Chat:** Interactive Q&A interface to query specific details within uploaded documents.
- **🛡️ Production Ready:** Full Dockerization and automated CI/CD deployment pipeline.

---

## 🧠 System Architecture & MLOps Pipeline

### Data Flow
1. **Ingestion:** PDF text extraction using `PyPDF2`.
2. **Indexing:** Embedding generation via `Sentence Transformers`.
3. **Storage:** High-performance vector retrieval using `FAISS`.
4. **Orchestration:** `LangChain` coordinating the RAG logic.
5. **Inference:** `Google Gemini / LLaMA` processing queries via shared logic.

### Deployment Workflow
`Local Git Push` ➔ `GitHub Actions` ➔ `Docker Build` ➔ `Hugging Face Spaces`

---

## 🛠️ Tech Stack

| Category | Tools |
| :--- | :--- |
| **LLM / RAG** | LangChain, Google Gemini API, LLaMA |
| **Vector DB** | FAISS (Facebook AI Similarity Search) |
| **Frontend** | Streamlit |
| **Backend** | FastAPI |
| **DevOps** | Docker, GitHub Actions (CI/CD) |
| **Libraries** | PyPDF2, Pandas, Sentence-Transformers |

---

## 📂 Project Structure

```text
rag_resume_ai/
├── app/               # Core RAG logic, embeddings & qa_chains
├── api/               # FastAPI implementation & shared logic
├── ui/                # Streamlit UI components
├── faiss_index/       # Pre-built vector database
├── .github/workflows/ # CI/CD automation (ci.yml)
├── Dockerfile         # Container configuration
└── requirements.txt   # Production dependencies

## ⚙️ Installation & Setup
**1️⃣ Clone and Environment**
git clone [https://github.com/your-username/rag-resume-ai.git](https://github.com/your-username/rag-resume-ai.git)
cd rag-resume-ai
python -m venv venv
venv\Scripts\activate on Windows
pip install -r requirements.txt

**2️⃣ Running Locally**
**Mode A: Monolithic (Streamlit only)**
streamlit run rag_resume_ai/ui/streamlit_app.py

**Mode B: Microservices (FastAPI + Streamlit)**
# Terminal 1
uvicorn rag_resume_ai.api.main:app --reload
# Terminal 2
streamlit run rag_resume_ai/ui/streamlit_app.py

**🐳 Docker Deployment**
docker build -t resume-ai .
docker run -p 8501:8501 resume-ai

Recommended for local testing of the full RAG pipeline:
