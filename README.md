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
---
I understand! You want the whole thing as a single, ready-to-use block so you don't have to piece it together.

Here is the complete, final version of your README.md. I have unified everything from the Hugging Face metadata at the top to the installation and Docker commands at the bottom into one single code block for you.

Markdown
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

[![Docker Support](https://img.shields.io/badge/Docker-Supported-blue.svg?logo=docker)](Dockerfile)
[![Hugging Face Space](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-yellow)](https://huggingface.co/spaces/Azar-Mhmd/ai-resume-intelligence)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An end-to-end **Generative AI & MLOps** project featuring a RAG (Retrieval-Augmented Generation) system. This platform automates ATS scoring, skill-gap analysis, and personalized interview preparation using Google Gemini and open-source embedding models.

## 🚀 Key Features

- **🎯 ATS Matcher:** Advanced semantic comparison between Resume (PDF) and Job Descriptions.
- **🔍 Skill Analytics:** Automated extraction of matched and missing technical skills.
- **🎤 Interview Coach:** Generates contextual interview questions based on JD and candidate experience.
- **💬 Resume Chat:** Interactive Q&A interface to query specific details within uploaded documents.
- **🛡️ Production Ready:** Full Dockerization and automated CI/CD deployment pipeline via GitHub Actions.

---

## 🧠 System Architecture & MLOps Pipeline

### Data Flow
1. **Ingestion:** PDF text extraction using `PyPDF2`.
2. **Indexing:** Embedding generation via `Sentence Transformers`.
3. **Storage:** High-performance vector retrieval using `FAISS`.
4. **Orchestration:** `LangChain` coordinating the RAG logic.
5. **Inference:** `Google Gemini` processing queries via a shared monolithic logic module.

### Deployment Workflow
`Local Git Push` ➔ `GitHub Actions` ➔ `Docker Build` ➔ `Hugging Face Spaces`

---

## 🛠️ Tech Stack

| Category | Tools |
| :--- | :--- |
| **LLM / RAG** | LangChain, Google Gemini API |
| **Vector DB** | FAISS (Facebook AI Similarity Search) |
| **Frontend** | Streamlit |
| **Backend** | FastAPI |
| **DevOps** | Docker, GitHub Actions (CI/CD) |
| **Libraries** | PyPDF2, Pandas, Sentence-Transformers, Torch |

---

## 📂 Project Structure

```text
rag_resume_ai/
├── app/               # Core RAG logic, embeddings & qa_chains
├── api/               # shared logic & FastAPI implementation
├── ui/                # Streamlit UI components
├── faiss_index/       # Pre-built vector database
├── .github/workflows/ # CI/CD automation (ci.yml)
├── Dockerfile         # Container configuration
└── requirements.txt   # Production dependencies

⚙️ Installation & Setup
1️⃣ Clone and Environment

# Clone the repository
git clone [https://github.com/Azar-Mhmd/ai-resume-intelligence.git](https://github.com/Azar-Mhmd/ai-resume-intelligence.git)
cd ai-resume-intelligence

# Create and activate virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

2️⃣ Running Locally
You can run the application in two different modes:

Mode A: Monolithic (Streamlit Only) — Recommended
This mode runs the UI and RAG logic in a single process (the cloud-native way):

streamlit run rag_resume_ai/ui/streamlit_app.py

Mode B: Microservices (FastAPI + Streamlit)
Useful for testing the raw API endpoints:

# Terminal 1: Backend
uvicorn rag_resume_ai.api.main:app --reload

# Terminal 2: Frontend
streamlit run rag_resume_ai/ui/streamlit_app.py

🐳 Docker Deployment
To replicate the production environment used in Hugging Face Spaces locally:

# Build the Docker image
docker build -t resume-ai .

# Run the container locally
docker run -p 8501:8501 resume-ai

Visit http://localhost:8501 to use the app.

👨‍💻 Author
Azarudeen Generative AI Engineer | Data Analyst (www.linkedin.com/in/mohamed-azarudeen-a34799165) | GitHub
