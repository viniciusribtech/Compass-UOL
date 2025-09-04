# lista contendo 250 números aleatórios e aplicando o método reverse:
import random

numeros = random.sample(range(1, 251), 250)

print("Lista original:")
print(numeros)

numeros.reverse()

print("\nLista invertida:")
print(numeros)

# lista de 20 animais, ordenando em ordem crescente e imprimindo um a um:
# Lista com 20 nomes de animais
animais = ["cachorro", "gato", "onça", "jacaré", "pássaro",
           "urso", "veado", "baleia", "leão", "tatu",
           "macaco", "gorila", "orangotango", "peixe", "capivara",
           "leopardo", "girafa", "elefante", "hipopótamo", "zebra"]

ordem_animais = sorted(animais)

print("Animais em ordem:")
[print(animal) for animal in ordem_animais]

with open("animais.txt", "w", encoding="utf-8") as arquivo:
    for animal in ordem_animais:
        arquivo.write(animal + "\n")