from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import rand, when
from pyspark.sql.functions import floor, col, array, lit

spark = SparkSession.builder.master("local[*]").appName("Exercício Spark").getOrCreate()

df_nomes = spark.read.csv(r"C:\Users\twvin\OneDrive\Área de Trabalho\nomes_aleatorios.txt", header= False)
df_nomes = df_nomes.withColumnRenamed("_c0", "nome")

df_nomes.printSchema()
df_nomes.show(10, truncate= False)

df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when((rand() < 0.33), "Fundamental")
    .when((rand() < 0.66), "Medio")
    .otherwise("Superior")
)

pais = [
    "Brasil", "Bolívia", "Guiana", "Argentina", "Peru",
    "Suriname", "Uruguai", "Equador", "Guiana Francesa", "Paraguai",
    "Colômbia", "Chile", "Venezuela"
]

pais_array = array([lit(p) for p in pais])

df_nomes = df_nomes.withColumn(
    "Pais",
    pais_array[floor(rand() * len(pais))]
)

df_nomes = df_nomes.withColumn(
    "AnoNascimento",
    floor(rand() * (2010 - 1945 + 1) + 1945)
)

df_select = df_nomes.select("Nome", "AnoNascimento").where(df_nomes["AnoNascimento"] >= 2000)
df_select.show(10, truncate=False)

df_nomes.createOrReplaceTempView("Pessoas")

df_select_sql = spark.sql("select Nome, AnoNascimento from Pessoas where AnoNascimento >= 2000")
df_select_sql.show(10, truncate=False)

df_millennials = df_nomes.filter(
    (col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994)
)

print("Número de 'millennials': ", df_millennials.count())

df_nomes.createOrReplaceTempView("Pessoas")

df_millennials_sql = spark.sql("""
    select count (*) as quant_millenials
    from Pessoas
    where AnoNascimento between 1980 and 1994
""")

df_millennials_sql.show()

df_geracoes = spark.sql("""
    select
        Pais,
        case
            when AnoNascimento between 1944 and 1964 then 'Baby Boomers'
            when AnoNascimento between 1965 and 1979 then 'Geração X'
            when AnoNascimento between 1980 and 1994 then 'Millennials'
            when AnoNascimento between 1995 and 2015 then 'Geração Z'
        end as Geracao,
        count (*) as quantidade 
    from Pessoas
    group by Pais, Geracao
    order by Pais ASC, Geracao ASC, Quantidade ASC                     
""")

df_geracoes.show(50, truncate= False)