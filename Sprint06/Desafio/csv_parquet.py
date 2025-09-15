# CÓDIGO QUE SERÁ EXECUTADO PELO GLUE

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from datetime import datetime
from pyspark.sql.functions import col, lower

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# lendo os dados csv
df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [args['S3_INPUT_PATH']]},
    format="csv",
    format_options={"withHeader": True, "separator": "|"}
)

#filtrando os gêneros a serem usados
df_filtrado = Filter.apply(
    frame=df,
    f=lambda x: 
        'genero' in x and 
        x['genero'] is not None and 
        ('action' in x['genero'].lower() or 
        'adventure' in x['genero'].lower())
)
#limitando os registros a 100, convertendo o DynamicFrame para dataframe temporariamente pra usar a função .limit()
if df_filtrado.count() > 0:
    spark_df = df_filtrado.toDF().limit(100)
    df_definitivo = glueContext.create_dynamic_frame.from_rdd(spark_df.rdd, spark_df.schema)
else:
    df_definitivo = df_filtrado

#data de hoje para particionar
data_hoje = datetime.now()
ano = data_hoje.strftime('%Y')
mes = data_hoje.strftime('%m')
dia = data_hoje.strftime('%d')

s3_output_path = f"s3://desafio-sprint6-vinicius/Trusted/Local/CSV/Parquet/Movies/{ano}/{mes}/{dia}/"

# escrevendo o parquet no bucket
glueContext.write_dynamic_frame.from_options(
    frame=df_definitivo,
    connection_type="s3",
    connection_options={"path": s3_output_path},
    format="parquet"
)
job.commit()