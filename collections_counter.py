"""
Colletions -> High-performance Container Datetypes.

Módulo Collections - Counter
Counter será útil quando precisa-se responder perguntas, como:

- Qual item apareceu mais?
- Quantas vezes cada valor apareceu?
- Quais são os valores repetidos?
- Qual palavra mais aparece em um texto?
- Qual produto mais vendido?
- Qual status mais comum

///////////////////////////////////////////////////////////

lista = [1,1,1,2,3,4,4,6,5,8,7,5,4,6,2,3,4,2,4,1,1,5,6,7]
contador = Counter(lista)
print(contador) #Counter({1: 5, 4: 5, 2: 3, 6: 3, 5: 3, 3: 2, 7: 2, 8: 1})

texto = 'banana split'
contador_texto = Counter(texto)
print(contador_texto)

print(contador_texto['a'])
print(contador_texto['s'])
print(contador_texto['n'])

lista = ['javascript', 'python', 'java', 'javascript', 'C#']
contador_lista = Counter(lista)
print(contador_lista)

# Para verificar o mais comum, use most_common(1)

print(contador_lista.most_common(1))

status_pedidos = [
    'pago',
    'pendente',
    'pago',
    'cancelado',
    'pago',
    'pendente'
]
contador_status_pedidos = Counter(status_pedidos)
print(contador_status_pedidos)

print(contador_status_pedidos.most_common(1))

texto = 
Python é uma linguagem muito usada para automação, dados, web e inteligência artificial.
Com Python, podemos trabalhar com listas, dicionários, conjuntos e arquivos.
Em projetos de dados, Python ajuda a extrair, transformar e organizar informações.
Quanto mais praticamos Python, mais entendemos como resolver problemas reais com código.

counter_letras = Counter(texto.lower())
counter_palavras = Counter(texto.lower().split())
# print(counter_texto)
print(counter_letras.most_common(5))
print(counter_palavras.most_common(5))


"""

from collections import Counter

contador = Counter({
    'python': 3,
    'dados': 2,
    'web': 1
})

print(list(contador.elements()))
# elements não mostra elementos com contagem 0 ou negativo.
