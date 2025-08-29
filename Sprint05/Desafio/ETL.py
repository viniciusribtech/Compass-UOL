import boto3

arquivo1 = r"C:\Users\twvin\OneDrive\Área de Trabalho\Filmes+e+Series\movies.csv"
arquivo2 = r"C:\Users\twvin\OneDrive\Área de Trabalho\Filmes+e+Series\series.csv"
bucket = "desafio-sprint5-vinicius"

s3 = boto3.client(
    "s3",
    aws_access_key_id = "ASIA4ETEZ2EN3KLEJOLT",
    aws_secret_access_key = "zIcc8KgzyKSNSEgXsF7rZdpwzrOcCsU1aQzQb1Uq",
    aws_session_token = "IQoJb3JpZ2luX2VjEFAaCXVzLWVhc3QtMSJIMEYCIQDaJeqGpJjyXHVOzzS4XBDNbuIWgbTRBfKRkeMtnFq8eQIhAKerYNvYSXWq7q4B703ND9RlnUZalml9ki4/UApX+rX2KqIDCKn//////////wEQABoMODM0NTA4ODA0Mzc5Igwe+iBWVsoRGZgu11Aq9gLGOSgslXGi0icuZUBpHT3/B0KDp/eQe6ZKQHuv0AiJJ/82DgiU2ZGnf1045j1yy18WwwA8P8D9o0Uv6QP2De2+/XtNobbfEXtQl8yBMwZkSNOKflBA1mZDDI4jwISTar5ghxLzxfBPH1wjeO7i6+JbVwH2Km6iqFKydiWfWFLneRJ3VdzTNNf0OaJokDljC+1vbJktYawmIk3PVIEF54E//1sd8j4QRRlWwFJKpwIrqRbvwqthET8wNfN0Qg2jC4IxEPjF5u9v+BuMkBAjQBcdZiCWUHCk6iDKo1toQfPC0gVVNWYZxo1kdmiZJ/luaeeGC2KyII7Cx4htcnZFoQ5fsl3kZ8BlsuLmb4uTQWduDrvkYgz1TH4ZAzcPbFO6YoQJUKMx83i3rnZUwsu/AO3rIgyRzJs4V0g0/QgHf4kPRt7/DzJ4WLA5v4zunzMx2DDhgeE7QvxNh4PyQWsH1Xhjps9Im/l0wMHeZFtgLAJT0hdm9tPzGzCU78HFBjqlAXi66GTRBKqsdE53bAl2GB66vAwuPybi08SykW/wiqhlglAdGEGhv0r7FcPpSWUlFZqq94E3f3EAsi0jmnS+xlWNWrMRKY8TcCKXAi0LBkjUEt/dHeF8LMHTI1bphNpTFZ8HUraANsPEAFEtZPaQJo+r0jZT89ZdalFmbWh5zwcKFUgzPxzG197r62S2d/tB5C1Dspcqnd5T8k8ZBm9oZvnbTE6aEw=="
)

s3.upload_file(arquivo1, bucket, "desafio-sprint5-vinicius/Raw/Local/CSV/Movies/2025/08/28/movies.csv")
s3.upload_file(arquivo2, bucket, "desafio-sprint5-vinicius/Raw/Local/CSV/Movies/2025/08/28/series.csv")

print("Arquivos enviados para o bucket ", bucket) # teste