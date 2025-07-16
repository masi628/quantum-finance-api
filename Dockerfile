
# Usa Python 3.10 come base (compatibile con Qiskit ≥1.0)
FROM python:3.10-slim

# Imposta directory di lavoro
WORKDIR /app

# Copia i file del progetto nella directory del container
COPY . /app

# Evita messaggi interattivi da pip
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1

# Installa dipendenze di sistema per Qiskit
RUN apt-get update && apt-get install -y \
    build-essential \
    libblas-dev \
    liblapack-dev \
    gfortran \
    libatlas-base-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Installa pacchetti Python
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Espone la porta (necessaria per DigitalOcean)
EXPOSE 8080

# Comando di avvio (FastAPI con Uvicorn)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
