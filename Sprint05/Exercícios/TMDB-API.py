import requests
import pandas as pd
from IPython.display import display

#chaves ocultadas depois da execução
chave_api= "xxxxx"
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key=xxxxx&language=pt-BR"

response = requests.get(url)
data = response.json()
filmes = []

for movie in data ["results"]:
    df = {'Título': movie['title'],
          'Idioma original': movie['original_language'],
          'Popularidade': movie['popularity'],
          'Data': movie['release_date'],
          'Visão geral': movie['overview'],
          'Votos': movie['vote_count'],
          'Média de votos': movie['vote_average']
          }
    filmes.append(df)
df = pd.DataFrame(filmes)
display(df)