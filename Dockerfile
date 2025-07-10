FROM python:3.10-slim

WORKDIR /app

# 🔹 Copia PRIMA requirements.txt nella root del container
COPY requirements.txt .

# 🔹 Installa i pacchetti
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 🔹 Poi copia tutta l'app (dopo i pacchetti: ottimizza cache Docker)
COPY ./app /app

# 🔹 Comando di avvio (porta 8000 è ok se DigitalOcean la mappa)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
