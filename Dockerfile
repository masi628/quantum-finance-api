
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN rm -rf /usr/local/lib/python*/dist-packages/*-info
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./app /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
