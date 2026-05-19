"""
Mapas -> São estruturas do tipo chave/valor.
Em python, essa estrutura é chamada de dicionário (dict).

Dicionários em Python são representados por chaves {}

receita = {'jan': 100, 'fev': 220, 'mar': 300}
# Iterar sobre dicionários:
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R${receita[chave]}')

# Acessando as chaves
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores 
print(receita.values())

for values in receita.values():
    print(values)

# Desempacotamento de dicionários:
print(receita.items())

for key, value in receita.items():
    print(f'Chave={key} e Valor={value}')

Métodos de soma, valor máximo e mínimo

print(sum(receita.values))
print(max(receita.values))
print(min(receita.values))
"""