
FROM python:3.11-slim

# Crea virtualenv per evitare conflitti
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

# Installa le dipendenze
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia l'app dopo aver installato le dipendenze (per cache Docker)
COPY ./app /app

# Espone la porta 8080
EXPOSE 8080

# Comando di avvio
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
