"""
Conjuntos

- Conjuntos em qualquer lingaguem de programção, estamos fazendo
referência a 'Teoria dos Conjuntos'

 - Conjuntos é chamado de Sets em Python.
Dito isso, da mesma forma que na matemática:
- Sets não possuem valores duplicados;
- Sets não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, 
conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles.
Quando não precisamos nos preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos(Sets) e Mapas(Dicionários) em Python:
    - Dicionário tem chave/valor;
    - Conjunto tem apenas valor;


Conjuntos - Sets são usados em situações especificas:
    - Remover Duplicados
    - Comparar grupos de dados
    - Verificar pertencimento
    - Fazer união/interseção/diferença


# Definindo um conjunto:
# Forma 1:
s = set([1,2,3,4,5,6,7,2,3]) # Temos dois valores repetidos.
print(s) # {1, 2, 3, 4, 5, 6, 7} --> Não retorna duplicados.
# Remove os valores duplicados.

# Forma 2 - Mais comum:
s = {1,2,3,4,5,6,7,1,2}
print(s)
print(type(s))


# Validação: 
usuarios_sistemas = {"André", "Enzo", "Diego"}
usuarios_pagantes = {"Clóvis", "Enzo", "André"}

print(usuarios_sistemas & usuarios_pagantes)

# Criando set a partir de Lista
# Para transformar em set, precisa-se armazenar em uma variável
lista = [1,2,3,3,1,5,7,9,1,3]
lista_set = set(lista)
print(lista_set)
print(type(lista_set))

# Métodos principais:
numeros = {1,2,3,4,5,6}
numeros.add(7) # add -- Adiciona
print(numeros)
numeros.remove(1) # remove -- Remove
print(numeros)
numeros.discard(5) ## discard -- Remove (Em caso de erro, ignora.)
print(numeros)

# Parte mais importante de Conjuntos(Sets) são operações matemáticas.
a = {1,2,3,4}
b = {3,4,5,6}

print(a | b) # | representado como UNIÃO dos valores.
# ou
print(a.union(b)) # Outra maneira de realizar UNIÃO.

print(a & b) # & representado como INTERSEÇÃO dos valores.
# ou
print(a.intersection(b)) # Outra maneira de realizar INTERSEÇÃO.

print(a - b) # - representado como DIFERENÇA em relação ao segundo valor.
# ou
print(a.difference(b)) # Outra maneira de realizar DIFERENÇA. 

print(a ^ b) # ^ representado como DIFERENÇA SIMÉTRICA.
# ou
print(a.symmetric_difference(b)) # Outra maneira de realizar DIFERENÇA SIMÉTRICA.



"""
numeros = [1, 2, 3, 2, 4, 5, 1, 6, 4, 7]
numerors_set = set(numeros)
print(numerors_set)
print(type(numerors_set))
# Os valores repetidos sumiram pois se trata de um Conjunto. Em Conjuntos
# Não existe valores duplicados.

python = {'Ana', 'Carlos', 'João', 'Marcos'}
javascript = {'Carlos', 'Marcos', 'Pedro', 'Lucas'}
print(python | javascript)
print(python & javascript)
print(python - javascript)
print(javascript - python)
print(python ^ javascript)

permissoes_sistema = {'criar', 'editar', 'deletar', 'visualizar', 'exportar'}
permissoes_usuario = {'editar', 'visualizar'}
print(permissoes_usuario)
print(permissoes_sistema - permissoes_usuario)
permissoes_usuario.add('exportar')
print(permissoes_usuario)
permissoes_usuario.discard('editar')
print(permissoes_usuario)








