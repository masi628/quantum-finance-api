FROM python:3.10-slim

# Virtualenv per isolare le dipendenze
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

# Installa i requirements PRIMA per caching Docker
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Poi copia i file app
COPY ./app /app

EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
