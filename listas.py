"""
Listas

Listas em Python funciona como vetores/mnatrizez (arrays).
Listas são DINÂMICAS e também podem receber QUALQUER tipo de dado.

- Dinâmico: Não possuem tamnho fixo. ou seja, podemos criar a lista e
simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos
colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes []

type([]) # -> Lista

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ',]
lista3 = []
lista4 = list(range(11))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista5 = list('Geek University')
lista6 = [1, 2, 3]
curso = 'Programação em Python: Essencial'
curso1 = 'Programação,em,Python:,Essencial'
curso2 = ['Programação', 'em', 'Python:', 'Essencial']

# Podemos checkar facilmente se determinado valor está contido na lista.
num = 2
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista:
lista1.sort(reverse = True)
print(lista1)
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de valor em uma lista.
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em lista


Para adicionar um elemento na lista, utilizamos a função append:
# append() adiciona 1 elemento ao final da fila.
lista1.append(50)
print(lista1)

# extend() adiciona +1 elementos final da fila.
lista1.extend([51, 52, 53])
print(lista1)

# Também pode incrementar
lista1 += 60, 61, 62
lista1.sort()
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
lista1.insert(6, 15)
#            ( Indíce, Valor )
print(lista1)

# Podemos facilmente juntar duas listas
lista6 = lista1 + lista2
print(lista6)

# Para inversão da lista, usar .reverse()
# Forma 1 usando reverse
lista1.reverse()
print(lista1)
# Forma 2 usando slice
print(lista1[::-1])

# Criando uma lista nova com dados de outra:
lista6 = lista2.copy()
print(lista6)

# Saber a quantidade de índices de uma lista:
print(len(lista1))

# Remover o último elemento da lista:
print(lista5)
lista5.pop()
print(lista5)

# Remover um valor pelo índice:
print(lista1)
lista1.pop(1)
print(lista1)
lista1.pop(0)
print(lista1)
# Se não houver um elemento no índice informado, teremos um erro IndexError

# Remover um valor especifico:
lista1.remove(100)
print(lista1)
# Se não houver o valor especificado, teremos um erro ValueError

# Remover todos os elementos (zerar a lista)
print(lista1)
lista1.clear()
print(lista1)

# Podemos repetir elementos em uma lista:
lista6 *= 3
print(lista6)

# Transformar string em lista
curso = 'Programação em Python: Essencial'
curso = curso.split()
# -> Por padrão o split separa os elementos pelo espaço entre elas.
print(curso)

# Transformar string em lista com separação específica.
curso1 = curso1.split(',')
print(curso1)

# Convertendo uma lista em uma string.
print(lista2)
# Irá pegar a lista e adicionar o espaço entre cada elemento.
curso3 = ' '.join(curso2)
print(curso3)

# Irá pegar a lista e adicionar o $ entre cada elemento.
curso3 = '$'.join(curso2)
print(curso3)

# Podemos realmente colocar qualquer tipo de dado em uma lista.
lista7 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 456_421_654]

# Iterando sobre listas.
# Exemplo 1 For

# Iterar com números
soma = 0
for elemento in lista1:
    print(elemento)
    soma += elemento
print(soma)

#Iterar com string
soma = ''
for elemento in lista2:
    print(elemento)
    soma += elemento
print(soma)


# Exemplo 2 While

carrinho = []
produto = ''


while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para encerrar: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros_lista = [num1, num2, num3, num4, num5]
print(numeros_lista)

# Em Listas, fazemos acessos aos elementos de forma indexada

cores = ['verde', 'azul', 'amarelo', 'branco']
print(cores[0]) # verde
print(cores[1]) # azul
print(cores[2]) # amarelo
print(cores[3]) # branco

# Para iniciar de forma reversa, inicia-se em -1
print(cores[-1]) # branco
print(cores[-2]) # amarelo

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

cores = ['verde', 'amarelo', 'azul', 'branco']

# Gerar indíce em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Outros métodos não tão importantes mas também úteis.
# Encontrar o índice de um elemento na lista.

numeros = [5,6,7,5,8,9,10]
# Em qual índice está o valror 6?
print(numeros.index(6))
# Em qual índice está o valror 9?
print(numeros.index(9))

# Fazer buscas dentro de um range, com um valor, a partir de um índice.
print(numeros.index(9, 2)) # Buscanso a partir do índice 2 o valor 9
print(numeros.index(9, 2)) # Buscanso a partir do índice 3 o valor 9


# Fazer buscas dentro de um range, início/fim
# Buscar o índice do valor 8, entre os índices 3 e 6
print(numeros.index(8, 1, 5)) 

# Revisão de slice
# LISTA[inicio/fim/passo] as palavras serão ':' ou números
# LISTA[::1] -- Passo de 1 em 1
# RANGE(inicio/fim/passo) as palavras serão ':' ou números
# RANGE(::1) -- Passo de 1 em 1

# Trabalhando com Slice de listas com o parâmetro início
lista = [0,1,2,3,4,5,6,7,8]
print(lista[1:6:2]) # Iniciando do índice 1 e indo até o final

# Trabalhando com Slice de listas com o parâmetro fim
lista = [0,1,2,3,4,5,6,7,8]
print(lista[:6]) # Iniciando do índice 1 e indo até o final

# Invertendo valores em uma lista
nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['Geek', 'University']
nomes.reverse()
print(nomes)

# Soma, Valor Máximo, Valor Mínimo, Tamanho.
# Para 'Valor Máximo' e 'Valor Mínim'o os valores precisarão ser 
# Inteiros ou reais.
lista = [1,2,3,4,5,6,7,8,9]

print(sum(lista)) # Soma
print(max(lista)) # Valor Máximo
print(min(lista)) # Valor Mínimo
print(len(lista)) # Tamanho da lista em valores, não em ***Índex***!!!!

# Transformar uma lista em uma tupla
lista = [1,2,3,4,5,6,7,8,9]
print(lista)
print(type(lista))
tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas
lista = [1,2,3,5000]
num1, num2, num3, num4 = lista
print(num1)
print(num2)
print(num3)
print(num4)

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Shallow Copy: 
# Irá criar uma nova lista com valores da antiga. 
# A lista externa é diferente na memória.
# Para listas simples, funciona como uma cópia independente.
lista = [1,2,3]
print(f'Variável Lista {lista}')
nova = lista.copy()
print(f'Variável Nova {nova}')
nova.append(4)
print(f'Variável Nova Append {nova}')

# Referência / atribuição direta:
# Não cria uma nova lista.
# Apenas aponta a nova variável para o mesmo objeto na memória.
# Nova ----> Lista
lista = [1,2,3] # ID 55564
print(f'Variável Lista {lista}')
nova = lista
nova.append(4)
print(f'Variável Lista {lista}')
print(f'Variável Nova {nova}')

# Deep Copy
# Cria uma cópia completa e indepente da lista original.
# Caso tenha outras listas dentro dela, copiará todas.
# Criará uma nova variável na memória.
# Para usar deep copy, precisamos improtar o módulo copy.
import copy

lista = [[1, 2], [3, 4]]
nova = copy.deepcopy(lista)
print(id(lista))
print(id(nova)) 
nova[0].append(10)
print(lista)
print(nova)

"""
