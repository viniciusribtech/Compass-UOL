from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("LerParquet") \
    .getOrCreate()

#o objetivo é ler o parquet que baixei do meu próprio bucket, da camada Trusted Zone, pra acessar as colunas presentes
df = spark.read.parquet(r"C:\Users\twvin\Downloads\part-00000-33a6e641-bd01-485e-abe1-7dbc2a992b31-c000.snappy.parquet")

df.show(10)
df.printSchema()