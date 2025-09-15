import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from datetime import datetime
from pyspark.sql.functions import array_contains
from pyspark.sql.functions import explode

args = getResolvedOptions(sys.argv, ["JOB_NAME", "S3_INPUT_PATH"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

#lendo o JSON do bucket
df = spark.read.option("multiline", "true").json(args["S3_INPUT_PATH"])

#com ajuda de uma IA, utilizei a função 'explode', que muda os elementos de um array, separando-os por vírgula
filmes_df = df.select(explode("results").alias("filme"))

#extraindo colunas
filmes_expandidos = filmes_df.select(
    "filme.adult",
    "filme.backdrop_path", 
    "filme.genre_ids",
    "filme.id",
    "filme.original_language",
    "filme.original_title",
    "filme.overview",
    "filme.popularity",
    "filme.poster_path",
    "filme.release_date",
    "filme.title",
    "filme.video",
    "filme.vote_average",
    "filme.vote_count"
)

# filtrando gêneros, na API do TMDB, os gêneros são divididos por IDs, sendo 28 = ação e 12 = aventura
df_filtrado = filmes_expandidos.filter(
    array_contains(filmes_expandidos["genre_ids"], 28) | array_contains(filmes_expandidos["genre_ids"], 12)
)

#data de hoje para particionar
data_hoje = datetime.now()
ano = data_hoje.strftime('%Y')
mes = data_hoje.strftime('%m')
dia = data_hoje.strftime('%d')

s3_output_path = f"s3://desafio-sprint6-vinicius/Trusted/API/JSON/TMDB/Parquet/Movies/{ano}/{mes}/{dia}/"

df_filtrado.write.mode("overwrite").parquet(s3_output_path)

job.commit()