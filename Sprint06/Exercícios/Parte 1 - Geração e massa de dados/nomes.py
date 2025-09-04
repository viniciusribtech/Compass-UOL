import random
import time
import os
import names

qtd_nomes_unicos = 100
qtd_nomes_aleatorios = 350
random.seed(33)

aux = []

for i in range(qtd_nomes_unicos):
    aux.append(names.get_full_name())

print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios...")

dados = []

for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

with open("nomes_aleatorios.txt", "w", encoding = "utf-8") as arquivo:
    for nome in dados:
        arquivo.write(nome + "\n")

print ("Arquivo gerado.")