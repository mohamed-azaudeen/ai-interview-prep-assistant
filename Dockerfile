FROM python:3.10-slim

WORKDIR /app

COPY requirments.txt .
RUN pip install --no-cache-dir -r requirments.txt

COPY . .

EXPOSE 8501

ENV PYTHONPATH=/app

CMD ["streamlit", "run", "rag_resume_ai/ui/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]