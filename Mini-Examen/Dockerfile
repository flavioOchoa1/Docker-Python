FROM python:3.11-alpine
WORKDIR /app
#copia de archivos
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "script-1-.py"]
