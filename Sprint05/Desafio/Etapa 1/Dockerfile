FROM python:3.11-slim

WORKDIR /app

COPY ETL.py .

RUN pip install boto3

VOLUME /app/data

CMD ["python","ETL.py"]