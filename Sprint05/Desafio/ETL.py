import boto3

arquivo1 = "/app/data/movies.csv"
arquivo2 = "/app/data/series.csv"
bucket = "desafio-sprint5-vinicius"

s3 = boto3.client(
    "s3",
    aws_access_key_id = "xxxxx",
    aws_secret_access_key = "xxxxx",
    aws_session_token = "xxxxx"
)

s3.upload_file(arquivo1, bucket, "desafio-sprint5-vinicius/Raw/Local/CSV/Movies/2025/08/28/movies.csv")
s3.upload_file(arquivo2, bucket, "desafio-sprint5-vinicius/Raw/Local/CSV/Movies/2025/08/28/series.csv")

print("Arquivos enviados para o bucket ", bucket) # teste