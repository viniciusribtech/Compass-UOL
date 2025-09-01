import json
import boto3
import requests

api_key = "xxxxx"
bucket = "desafio-sprint5-vinicius"
regiao_aws = "us-east-1"


s3 = boto3.client(
    "s3", 
    region_name= regiao_aws)

def lambda_handler(event, context):

    url = "https://api.themoviedb.org/3/movie/top_rated"

    todos_os_filmes = []

# cada chamado aceita 20 registros por página, então 5x20 = 100
    for pagina in range(1, 6):
        parametros = {
        "api_key": api_key,
        "language": "pt-BR",
        "page": pagina
    }

    resposta = requests.get(url, params=parametros)

    if resposta.status_code != 200:
        return {
            "statusCode": resposta.status_code,
            "body": "Erro ao consultar TMDB"
        }

    dados = resposta.json()

    caminho_arquivo = "Raw/API/JSON/TMDB/tmdb_populares.json"

    s3.put_object(
        Bucket=bucket,
        Key=caminho_arquivo,
        Body=json.dumps(dados, indent=4),
        ContentType="application/json"
    )

    return {
        "statusCode": 200,
        "body": f"Arquivo salvo no S3: {caminho_arquivo}"
    }