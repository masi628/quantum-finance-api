FROM python:3.10-slim

# Crea cartella app
WORKDIR /app

# Copia tutto il progetto
COPY . /app

# Aggiorna pip e installa solo Qiskit ≥1.0
RUN pip install --upgrade pip && \
    pip install qiskit qiskit-finance fastapi uvicorn

# Comando di avvio
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
