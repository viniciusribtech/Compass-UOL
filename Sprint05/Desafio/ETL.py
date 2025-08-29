import boto3

arquivo1 = "/app/data/movies.csv"
arquivo2 = "/app/data/series.csv"
bucket = "desafio-sprint5-vinicius"

s3 = boto3.client(
    "s3",
    aws_access_key_id = "ASIA4ETEZ2ENQTRJ4FSI",
    aws_secret_access_key = "Yi2jXcyXdBwaGxkAlu+uhYI1KyELmlonUU/e9yc1",
    aws_session_token = "IQoJb3JpZ2luX2VjEGcaCXVzLWVhc3QtMSJHMEUCIQDswo1cVQQRdAG1KakIV9n5IeQP2d8sECYcCkNpct6QgAIgG3aiPbgoGz4dUxwlq8x9tB91muogRcB2+s4qoDtfJR0qogMIwP//////////ARAAGgw4MzQ1MDg4MDQzNzkiDNbfEEYK8GXFAD7gjir2AqT/L9jx0nHQHNBqjt8mXDdd+JSXmOlnhaYHUyyemd2FaLDj8Ighei6jsl2amI0U8YR+jlp+VUmzqXUUdBwgG7Z0JguDhB1vnMYRhWBUvmcsAhO1tYD+1vScM8+tBolP+QMB3GKhlDY/gciVqSti56FmtX9F8jDwQmF2Hl98BXYDWlR6p6Ysz3xEyb5fF4OcvdQV5nzY8AuGXtOeqrZhGEnAsdROTLs4DZwW7yKxE9s4DJngpGZuR6pcHvKMbM8vMsJHwUx4b1Xko6cKP/esl32EwO+XPCFgoKZq1+EKwRjCO8tW/Y7uc7VJ6DWM2CIMHTwa7vhOVOgputexNKLS4HQRY7gBPpzGeFhRyo2QlbewcWAuydfU0/UXYDisyTF+/wJv+H/gLytqo8jmOHJaGnPICsJndCBX8WuSxjmNNTQWaWL7d4bgX67AHkG69yd5VZki8CUi4kocI1b/3KPBYKD3msRuQIcNmMMQijrxR9n4VT3P9rtJMJeCx8UGOqYBK1Cm/HprYQ5yz5YeYBHwdKG7U3kI51HkV6hdKwkSOm1mtnCWKvuijJjx063101bC3Oq+TdRKx9ZblGhTruTevfqQZstzyp3vbxJESwQoLdpKS6KsOoer1zdWonfvT5QfkQ+JgKrw2HiSAKggm7S6i7PyiENNkccdjM1TbSaKqegRDi5Kxd8CXmxPK2s1jER8gTnw45n3r3XIMGD/H//puMlUJJMLUw=="
)

s3.upload_file(arquivo1, bucket, "desafio-sprint5-vinicius/Raw/Local/CSV/Movies/2025/08/28/movies.csv")
s3.upload_file(arquivo2, bucket, "desafio-sprint5-vinicius/Raw/Local/CSV/Movies/2025/08/28/series.csv")

print("Arquivos enviados para o bucket ", bucket) # teste