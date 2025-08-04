FROM python:3.11-slim

WORKDIR /app

COPY job.py .

RUN pip install pandas matplotlib

CMD ["python", "job.py"]