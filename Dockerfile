FROM python:3.10-slim

WORKDIR /app

COPY . /app

# Installa dipendenze
RUN apt-get update && apt-get install -y \
    build-essential \
    libblas-dev \
    liblapack-dev \
    gfortran \
    libatlas-base-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Porta esposta
EXPOSE 8080

# Comando corretto per avviare FastAPI da /app/main.py
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

