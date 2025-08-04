import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/volume/csv_limpo.csv")

# Q1 - Qual é a artista que mais aparece nessa lista e possui a maior média de seu faturamento bruto?

cont = df['Artist'].value_counts()
artista_freq = cont.index[0]
media = df.groupby('Artist')['Actual gross'].mean()
artista_maior_media = media.idxmax()
resposta_1 = "Artista que mais aparece: " + artista_freq + " \nMaior média de faturamento bruto: " + artista_maior_media

# Q2 - Das turnês que aconteceram dentro de um ano, qual a turnê com a maior média de faturamento bruto?

turne_um_ano = df[df['Start year'] == df['End year']] #cria uma nova "tabela" com apenas turnes de um ano de duração
turne_mais_lucro = turne_um_ano.loc[turne_um_ano['Average gross'].idxmax()]
resposta_2 = f"Turnê: {turne_mais_lucro['Tour title']} \nArtista: {turne_mais_lucro['Artist']} \nMédia: {turne_mais_lucro['Average gross']}"

# Q3 - Quais são as 3 turnês que possuem o show (unitário) mais lucrativo? Cite também o nome de cada artista e o valor por show.
# Utilize a coluna "Adjusted gross (in 2022 dollars)". Caso necessário, crie uma coluna nova para essa conta.
df['Faturamento por show'] = df['Adjustedgross (in 2022 dollars)'] / df['Shows']

df_ordenado = df.sort_values('Faturamento por show', ascending=False)
top3 = df_ordenado.head(3) # 3 primeiras colunas da ordem decrescente acima

artistas = list(top3["Artist"])
turnes = list(top3["Tour title"])
valores = list(top3["Faturamento por show"])

resposta_3 = "3 shows mais lucrativos:\n"
for artista, turne, valor in zip(artistas, turnes, valores): #une as listas
    resposta_3 += f"{artista} - {turne}\n{valor:.2f}\n"

# criando o arquivo "respostas.txt"

arquivo = open("/volume/respostas.txt", "w", encoding="utf-8")
arquivo.write("Q1:\n--- " + resposta_1 + "\n\n")
arquivo.write("Q2:\n--- " + resposta_2 + "\n\n")
arquivo.write("Q3:\n--- " + resposta_3 + "\n")
arquivo.close()

# Q4 - Para a artista que mais aparece nessa lista e que tenha o maior somatório de faturamento bruto, 
# crie um gráfico de linhas que mostra o faturamento por ano da turnê. Apenas os anos com turnês.

soma_fat = df.groupby('Artist')['Actual gross'].sum()
artista_1 = soma_fat.idxmax()
df_1 = df[df['Artist'] == artista_1]
fat_ano = df_1.groupby('Start year')['Actual gross'].sum()

#plotando gráfico linha
plt.figure(figsize=(8,4))
plt.plot(fat_ano.index, fat_ano.values, marker='o')
plt.title("Faturamento da turnê da " +artista_1)
plt.xlabel("Ano")
plt.ylabel("Faturamento")
plt.grid(True)
plt.savefig("/volume/Q4.png")
plt.close()

# Q5 - Faça um gráfico de colunas demonstrando as 5 artistas com mais shows na lista.
soma_shows = df.groupby('Artist')['Shows'].sum()
top_5 = soma_shows.sort_values(ascending=False).head(5) #pega os 5 primeiros artistas da ordem decrescente

#plotando gráfico coluna
plt.figure(figsize = (10,6))
top_5.plot(kind='bar', color = 'blue')
plt.title("As 5 artistas com mais shows")
plt.xlabel("Artista")
plt.ylabel("Nº de Shows")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("/volume/Q5.png")
plt.close()