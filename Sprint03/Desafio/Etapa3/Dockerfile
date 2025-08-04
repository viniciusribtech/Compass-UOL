FROM python:3.11-slim

WORKDIR /app

COPY etl.py .

RUN pip install pandas

CMD ["python", "etl.py"]