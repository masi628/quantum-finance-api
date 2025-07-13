FROM python:3.10-slim

WORKDIR /app

# Copia requirements.txt e installa dipendenze
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia il resto dell'app
COPY ./app /app

# Esponi la porta 8080 (usata da DigitalOcean per health check)
EXPOSE 8080

# Comando di avvio corretto sulla porta giusta
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
