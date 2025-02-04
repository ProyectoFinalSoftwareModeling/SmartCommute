FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY /backend/ .
COPY /backend/repositories/ .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t smartcommute_python_backend:1.0.0 .
# docker run -d -p 8000:8000 --name smartcommute_python_backend smartcommute_python_backend:1.0.0