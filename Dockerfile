FROM python:3.11-alpine

WORKDIR /app

# Copiamos archivos
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "script.py"]
