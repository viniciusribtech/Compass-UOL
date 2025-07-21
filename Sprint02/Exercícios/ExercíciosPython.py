# Seção 3: Exercícios Python 1/4 - Básico
# Faça um programa que gere uma nova lista contendo apenas números ímpares.
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
impar = [num for num in a if num % 2 != 0]
print (impar)

# Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.
lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']
for palavra in lista:
    if palavra == palavra[::-1]:
        print("A palavra: " +palavra+ " é um palíndromo.")
    else:
        print("A palavra: "+palavra+" não é um palíndromo.")

# Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, nome in enumerate(primeirosNomes):
    sobrenome = sobreNomes[i]
    idade = idades[i]
    print(f"{i} - {nome} {sobrenome} está com {idade} anos.")

# Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados.

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def sem_duplicados(lista):
    return list(set(lista))
print(sem_duplicados(lista))

# Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

import json
with open('person.json', 'r', encoding= 'utf-8') as person:
    pessoa = json.load(person)
print(pessoa)

# Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento. Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def my_map(list, f):
    result = []
    for item in list:
        result.append(f(item))
    return result
def potencia_2(x):
    return x**2
print(my_map(list, potencia_2))

# Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.

with open('arquivo_texto.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha, end= '')

# Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.

def imprimir(*args, **kwargs):
    for valor in args:
        print(valor)
    for valor in kwargs.values():
        print(valor)

imprimir(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

# Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, Truese a lâmpada estiver ligada, False caso esteja desligada.

class Lampada:

    def __init__(self, ligada):
        self.ligada = ligada
    
    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        return self.ligada
    
lampada = Lampada(False)
lampada.liga()
print("A lâmpada está ligada?", lampada.esta_ligada())
lampada.desliga()
print("A lâmpada ainda está ligada?", lampada.esta_ligada())

# Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.

def somar(numeros):

    lista_numeros = numeros.split(",")
    
    soma = sum(int(numero) for numero in lista_numeros)
    
    return soma

lista = "1,3,4,6,10,76"

resultado = somar(lista)
print(resultado)

# Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo

def dividir(lista):
    tamanho = len(lista)
    parte = tamanho // 3
    parte1 = lista[:parte]
    parte2 = lista[parte:parte*2]
    parte3 = lista[parte*2:]
    return parte1, parte2, parte3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

p1, p2, p3 = dividir(lista)

print(p1, p2, p3)

# Crie uma lista com todos os valores (não as chaves!) e coloque numa lista de forma que não haja valores duplicados.

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

nova_lista = []

for valor in speed.values():
    if valor not in nova_lista:
        nova_lista.append(valor)

print(nova_lista)

# Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo

import random

random_list = random.sample(range(500), 50)

random_list.sort()
meio = len(random_list) // 2
if len(random_list) % 2 == 0:
    mediana = (random_list[meio - 1] + random_list[meio]) / 2
else:
    mediana = random_list[meio]
media = sum(random_list) / len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f"Media: {round(media, 2)}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")

# Imprima a lista abaixo de trás para frente.

lista = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(lista[::-1])

# PARTE 2
# Seção 4: Exercícios Python 2/4 - Avançado
# Implemente duas classes, Pato e Pardal , que herdam de uma superclasse chamada Passaro as habilidades de voar e emitir som.

class Passaro:
    def voar(self):
        print("Voando...")
    def som(self):
        pass

class Pato(Passaro):
    def som(self):
        print("Pato emitindo som...")
        print("Quack Quack")

class Pardal(Passaro):
    def som(self):
        print("Pardal emitindo som...")
        print("Piu Piu")

print("Pato")
pato = Pato()
pato.voar()
pato.som()
print("Pardal")
pardal = Pardal()
pardal.voar()
pardal.som()

# Crie uma classe chamada Pessoa, com um atributo privado chamado nome (declarado internamente na classe como __nome) e um atributo público de nome id.

class Pessoa:
    def __init__(self, id):
        self.id = id
        self.__nome = None  

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
        
pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)

# Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos).
class Calculo:
    def somar(self, x, y):
        return x + y

    def subtrair(self, x, y):
        return x - y

x = 4
y = 5

cal = Calculo()
print(f"Somando: {x}+{y} = {cal.somar(x, y)}")
print(f"Subtraindo: {x}-{y} = {cal.subtrair(x, y)}")

# Crie uma classe Ordenadora que contenha um atributo listaBaguncada e que contenha os métodos ordenacaoCrescente e ordenacaoDecrescente.
# Instancie um objeto chamado crescente dessa classe Ordenadora que tenha como listaBaguncada a lista [3,4,2,1,5] e instancie um outro objeto, decrescente dessa mesma classe com uma outra listaBaguncada sendo [9,7,6,8].
# Para o primeiro objeto citado, use o método ordenacaoCrescente e para o segundo objeto, use o método ordenacaoDecrescente.

class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)

    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada, reverse=True)

crescente = Ordenadora([3, 4, 2, 1, 5])
decrescente = Ordenadora([9, 7, 6, 8])

print(crescente.ordenacaoCrescente())
print(decrescente.ordenacaoDecrescente())

# PARTE 3
# Seção 4: Exercícios de Python - 3/4 - Avançado II
# Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
arquivo = open("number.txt", "r")
linhas = arquivo.readlines()
arquivo.close()

todos_os_numeros = list(map(lambda linha: int(linha), linhas))

pares = list(filter(lambda n: n % 2 == 0, todos_os_numeros))

ordenados = sorted(pares, reverse=True)

cinco_maiores = ordenados[:5]

soma_dos_cinco = sum(cinco_maiores)

print(cinco_maiores)
print(soma_dos_cinco)

# A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 

from functools import reduce

def calcula_saldo(lancamentos) -> float:
    valores = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)
    saldo = reduce(lambda acc, val: acc + val, valores)
    return float(saldo)
    
lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]
print(calcula_saldo(lancamentos))

# A função calcular_valor_maximo deve receber dois parâmetros, chamados de operadores e operandos. Em operadores, espera-se uma lista de caracteres que representam as operações matemáticas suportadas (+, -, /, *, %), as quais devem ser aplicadas à lista de operadores nas respectivas posições. Após aplicar cada operação ao respectivo par de operandos, a função deverá retornar o maior valor dentre eles.

def calcular_valor_maximo(operadores, operandos):
    def operacao(simbolo, a, b):
        if simbolo == '+':
            return a + b
        elif simbolo == '-':
            return a - b
        elif simbolo == '*':
            return a * b
        elif simbolo == '/':
            return a / b
        elif simbolo == '%':
            return a % b

    combinados = zip(operadores, operandos)

    resultados = map(lambda item: operacao(item[0], item[1][0], item[1][1]), combinados)
    return max(resultados)


# Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. É o arquivo estudantes.csv de seu exercício.
# Não consegui resolver essa questão, o corretor automático da plataforma continuava exibindo o mesmo erro.

# Você foi encarregado de desenvolver uma nova feature  para um sistema de gestão de supermercados. O analista responsável descreveu o requisito funcional da seguinte forma

def maiores_que_media(conteudo: dict) -> list:
    soma_dos_precos = 0
    for preco in conteudo.values():
        soma_dos_precos += preco

    quantidade_de_produtos = len(conteudo)
    media = soma_dos_precos / quantidade_de_produtos

    produtos_acima_da_media = []
    for nome, preco in conteudo.items():
        if preco > media:
            produtos_acima_da_media.append((nome, preco))

    produtos_ordenados = sorted(produtos_acima_da_media, key=lambda item: item[1])

    return produtos_ordenados

produtos = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

resultado = maiores_que_media(produtos)
print(resultado)

# Generators são poderosos recursos da linguagem Python. Neste exercício, você deverá criar o corpo de uma função, cuja assinatura já consta em seu arquivo de início (def pares_ate(n:int):) .
# O objetivo da função pares_ate é retornar um generator para os valores pares no intervalo [2,n] . Observe que n representa o valor do parâmetro informado na chamada da função.

def pares_ate(n: int):
    numero = 2
    while numero <= n:
        yield numero
        numero += 2
for par in pares_ate(10):
    print(par)
