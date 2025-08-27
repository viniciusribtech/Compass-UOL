import os
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ContadorPalavras").getOrCreate()
sc = spark.sparkContext

#Lendo o README do repositório do Spark no Github:
os.system("wget https://raw.githubusercontent.com/apache/spark/master/README.md")

arquivo = sc.textFile("README.md")
contagem = arquivo.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
contagem.collect()

print("Quantidade de palavras: ")
for(word, count) in contagem.collect():
    print(f"{word}: {count}")

#Esse código foi executado linha por linha no Pyspark shell no Terminal de Comando, na pasta Evidências, estão os prints da execução