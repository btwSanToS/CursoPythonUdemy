"""
Módulo Collections - Named Tuple

Recap Tupla:
tupla = (1, 2, 3)
print(tupla[1])

Named Tuple -> São tuplas difereniadas, onde, especificamos um nome
para a mesma e também parâmetros.
"""
from collections import namedtuple
# Precisamos definir o nome e parâmetros.
# Forma 1 -- direto:
# cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 -- separado por vírgula:
# cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 -- incluídas
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando tupla
# Forma 1
zeus = cachorro(idade = 2, raca = 'Chow-Chow', nome = 'Zeus')
print(zeus[0]) # Buscando idade -- Indíce 0
print(zeus[1]) # Buscando raça -- Indíce 1
print(zeus[2]) # Buscando nome -- Indíce 2

# Forma 2
print(zeus.idade) # Buscando idade -- Indíce 0
print(zeus.raca) # Buscando raça -- Indíce 1
print(zeus.nome) # Buscando nome -- Indíce 2
