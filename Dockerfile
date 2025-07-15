# Usa una versione compatibile di Python
FROM python:3.11-slim

# Imposta la working directory
WORKDIR /app

# Evita warning relativi a pip usato da root
ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Copia i file delle dipendenze PRIMA per sfruttare cache Docker
COPY requirements.txt .

# Aggiorna pip e installa le dipendenze
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copia l'intero codice dell'app (dopo le dipendenze)
COPY ./app /app

# Espone la porta 8080 per la DigitalOcean health check
EXPOSE 8080

# Comando per eseguire l'app sulla porta 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
