"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por maps.

Dicionários são coleções do tipo chave/valor.
Ex de valor:
Chave: [0,1,2]
Valor: [1,2,3]

Em dicionários, eles ficarão explicitos, diferente de listas e tuplas.
Eles são representados por {}

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos chave:valor;
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

# Criação de dicionários
# Forma 1 (Mais comum)
paises = {
    'br': 'Brasil',
    'eua': 'Estados Unidos',
    'py': 'Paraguai'
}

print(paises)

# Forma 2 (menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

# Acessando elementos
# Forma 1: Acessando via chave. Da mesma forma que lista/tupla
print(paises['br'])
print(paises['eua'])
# print(paises['ru']) --> KeyError
# Tentar acessar utilizando uma chave que não existe, retornará erro (KeyError)

# Forma 2: Acessando via get - Recomendado*****
print(paises.get('br'))
print(paises.get('ru')) # --> None


pais = paises.get('br', 'Não Encontrado')
# Podemos definir um valor padrão caso não encontremos o objeto com a chave informada
# variavel.get('objeto', 'Mensagem' )
if pais:
    print(pais)


# Podemos verificar se determinada chave se encontra em um dicionário
# Buscar por Chave
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)
print('eua' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive:
# Lista, tupla, dicionário, como chaves de dicionários, etc.
# Tuplas são bastante usadas como chaves de dicionários por serem imutáveis
localidades = {
    (35.6895, 39.6917): 'Escritório em Tokyo',
    (25.4894, 56.7889): 'Escritório em Nova Iorque',
    (11.5674, 15.8795): 'Escritório em Dubai'
}

print(localidades)
print(type(localidades))

receita = {
    'jan': 100, 
    'fev': 120,
    'mar': 300
}
print(receita)

# Adicionar elementos em um dicionário
# Forma 1 - Mais comum
receita['abr'] = 350
print(receita)

# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)
# receita.update({'mai': 500})
print(receita)

# Atualizando dados em um dicionário.
# Forma 1
receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)

# CONCLUSÃO1: A forma de adicionar novos elementos ou atualizar dados é a mesma.
# CONCLUSÃO2: Em dicionários, NÃO podemos ter chaves repetidas.
# A atualização é feita na chave. Não podendo repetir a mesma.

receita = {
    'jan': 100, 
    'fev': 120,
    'mar': 300
}
print(receita)
# Remover dados de um dicionário
# Forma 1 - Mais comum
ret = receita.pop('mar')
print(ret)
print(receita)
# OBS1: Precisamos sempre informar a chave. Caso não encontre, retornará (KeyError)
# OBS2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2
del receita['fev']
print(receita) 
# OBS: Neste caso o valor removido não é retornado.

# Imagine que você tem um e-commerce, onde temos um carrinho de compras na qual
# adicionamos produtos.

Carrinho de compras:
    Produto 1:
        Nome:
        Quantidade:
        Preço:
    Produto 2:
        Nome:
        Quantidade:
        Preço

# 1 - Lista
carrinho = []
produto1 = ['Playstation', 1, 2300.00]
produto2 = ['God Of War 4', 1, 150.00]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho) # [['Playstation', 1, 2300.0], ['God Of War 4', 1, 150.0]]

# 2 - Tupla
produto1 = ('Playstation', 1 , 2300.00)
produto2 = ('God Of War 4', 1, 150.00)
carrinho = (produto1, produto2)
print(carrinho) # (('Playstation', 1, 2300.0), ('God Of War 4', 1, 150.0))

# 3 - Dicionário
carrinho = []
produto1 = {'nome': 'Playstation', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God Of War 4', 'quantidade': 1, 'preco': 150.00}
carrinho.append(produto1)
carrinho.append(produto2)
# [{'nome': 'Playstation', 'quantidade': 1, 'preco': 2300.0}, 
# {'nome': 'God Of War 4', 'quantidade': 1, 'preco': 150.0}]
print(carrinho)
# Com dicionário, adicionamos ou removemos dados com melhor retorno na sua visualização


# Métodos de dicionários:
d = {
    'a': 1,
    'b': 2,
    'c': 3
}
# Limpar o dicionário (Limpar dados)
d.clear()
print(d)

# Copiando um dicionário para outro
# Forma 1 # DeepCopy
novo = d.copy()
print(novo) # {'a': 1, 'b': 2, 'c': 3}
novo_valor = {'d': 4}
novo.update(novo_valor) # {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
print(novo)

#Forma 2 # ShallowCopy
novo = d
print(novo)
novo_valor = {'d': 5}
novo.update(novo_valor)
print(novo) # {'a': 1, 'b': 2, 'c': 3, 'd': 5}
print(d) # {'a': 1, 'b': 2, 'c': 3, 'd': 5}


# Forma não usual de criação de dicionários.
outro = {}.fromkeys('a','b')
print(outro)
usuario = {}.fromkeys(['nome', 'pontos','email',], 'Desconhecido')
print(usuario)
# O método fromkeys recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e atribuir 
# a está chave o valor informado.
veja = {}.fromkeys('tesla', 'valor')
print(veja) # {'t': 'valor', 'e': 'valor', 's': 'valor', 'l': 'valor', 'a': 'valor'}
veja1 = {}.fromkeys('teste', 'valor')
print(veja1) # {'t': 'valor', 'e': 'valor', 's': 'valor'}
# Caso acima de chaves duplicadas não se repetem.


# Forma não usual de criação de dicionários.
outro = {}.fromkeys('a','b')
print(outro)
usuario = {}.fromkeys(['nome', 'pontos','email',], 'Desconhecido')
print(usuario)
# O método fromkeys recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e atribuir 
# a está chave o valor informado.
veja = {}.fromkeys(range(1, 11), 'novo')
#{1: 'novo', 2: 'novo', 3: 'novo', 4: 'novo', 5: 'novo', 6: 'novo', 7: 'novo', 8: 'novo', 9: 'novo', 10: 'novo'}
print(veja)

"""
