"""
Loop e For

Loop -> Estrutura de repetição.
Serve para executar um mesmo bloco de código várias vezes.

For -> Uma estrutura de repetição usada para percorrer uma sequência
ou coleção de dados

Em python, o for percorre itens de algo iterável, como:
- range()
- strings
- listas
- tuplas
- dicionários

Sintaxe:
for variavel in sequencia:
    bloco de codigo

A cada repetição, a variável recebe um novo valor da sequência

for i in range(1,6):
    print(i)

nome = "André Santos"
for letra in nome:
    print(letra)

# Lista:
frutas = ["maçã", "banana", "uva"]

for fruta in frutas:
    print(fruta)

# Para soma:

numeros = [10, 20, 30]
soma = 0
for numero in numeros:
    soma += numero

print(soma)

# Forma de se pensar em um for:
for item in conjunto:
    faça alguma coisa com item
### Ou seja, item irá receber dados do conjunto em questão

Loop é uma repetição.
For repete percorrendo uma sequência.
While repete enquanto uma condição for verdadeira.
Todo loop precisa ter uma lógica para parar.

Utilizamos loops para iterar sobre sequências ou sobre valores.
Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1,10)


nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1,10)

# Exemplo for:
for i in range(5,14):
    print(nome[i])

# Para saber o índice e valor, use enumerate:
for i, v in enumerate(lista):
    print(f'Índice: {i}, Valor: {v}')

# Para descartar algo, use '_'
for _, v in enumerate(nome):
    print(v)


qntd = int(input("Quantas vezes esse loop deve rodar? "))
soma = 0

for n in range(1, qntd + 1):
    num = int(input(f'Informe o número {n}: '))
    soma += num
print(soma)

# Sem pular linha:
nome = "Geek University"
for l in nome:
    print(l, end='')
"""
for _ in range(5):
    for num in range(1,5):
        print("\U0001F60D" * num)





