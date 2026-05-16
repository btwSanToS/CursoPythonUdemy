"""
Tuplas (Tuple)

Tuplas são bastante parecidas com listas.
Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ();
2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla, 
ela não muda. Toda operação em uma tupla gera uma nova tupla;

# A tupla é definida pela vírgula ','

# Cuidado 1: As tuplas são representadas por parênteses, mas veja:
tupla1 = (1,2,3,4,5,6,7,8)
print(tupla1)
print(type(tupla1))

# Sem o parênteses também vai criar uma tupla;
tupla2 = 1,2,3,4,5,6,7,8
print(tupla2)
print(type(tupla2))

# Cuidado 2: Tuplas com um elemento.
tupla3 = (4) # Isso não é uma tupla -- Apenas um inteiro.
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # Isso é uma tupla
print(tupla4)
print(type(tupla4))

# CONCLUSÃO: Podemos concluir que tuplas são definidas pela vírgula
# e não pelo uso do partênteses
= 4 -> Não é tupla
= (4) -> Não é tupla
= 4, -> É tupla
= (4,) -> É tupla

# Podemos gerar uma tupla dinâmicamente com range(início, fim, passo)
tupla = tuple(range(1,30,2))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla
tupla = 'Geek University', 'Programação em Python: Essencial'
escola, curso = tupla
print(escola)
print(curso)
# OBS: Gera erro (ValueError / IndexError) se colocarmos um número
# diferente de elementos para desempacotar

# Métodos para adição e remoção de elementos nas tuplas não existem.
# Dado ao fato das tuplas serem imutáveis.

# Soma*, Valor Máximo*, Valor Mínimo* e Tamanho.
# Se os valores forem todos inteiros ou reais

tupla = (1,2,3,4,5,6,7,8,9)
print(max(tupla))
print(min(tupla))
print(sum(tupla))
print(len(tupla))

# Concatenação de Tuplas:

tupla1 = (1,2,3)
print(f'Tupla 1 {tupla1}')
tupla2 = (4,5,6)
print(f'Tupla 2 {tupla2}')
tupla3 = tupla1 + tupla2 # Tuplas são imutáveis.
print(f'Tupla 3 {tupla3}')
print(f'Valores de Tupla 1 não foram alteradas. {tupla1}')
print(f'Valores de Tupla 2 não foram alteradas. {tupla2}')

# Caso queira que uma tupla especifica receba dados de outra:
tupla1 += tupla2 # Tuplas são imutáveis, mas podemos sobrescrever seus valores.
print(f'Tupla 1 após incremento {tupla1}')

# Verificar se determinado elemento está contigo na tupla

tupla = (1,2,3)
print(3 in tupla)
print(4 in tupla)

tupla_string = ('André', 'Guilherme', 'Diego', 'Clóvis')
print('André' in tupla_string)

# Iterando sobre uma tupla
tupla = (1,2,3,59,78,549,55)

for n in tupla:
    print(n)

for i, n in enumerate(tupla):
    print(i, n)

# Contando elementos dentro de uma tupla:
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('a'))
print(tupla.count('S'))
print(tupla.count('E'))

escola = tuple('Geek University')
print(escola)
print(escola.count('e'))

# Dicas na utilização de Tuplas
# Devemos utilizar tupla sempre que não precisarmos modificar os dados
# contidos em uma coleção.
# Exemplo 1:
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
meses = tuple(mes.title() for mes in meses)
print(meses)

# O acesso a elementos de uma tupla também é semelhante a uma lista.
print(meses[5])

# Iterar com While
i = 0
while i < len(meses):
    print(meses[i])
    i += 1

# Verificar em qual índice um elemento está na tupla
print(meses.index('Junho', 2))
# OBS: Caso o elemento não exista, será gerado o erro (ValueError)


# Slicing
# tupla[inicio:fim:passo]
print(len(meses))
print(meses[2:11:1])


# Por quê utilizar tuplas?

# --> Tuplas são mais rápidas que listas. (Performance no código)
# Por conta de serem imutáveis, tornam-se mais rápiodas nas operações

# --> Tuplas deixam seu código mais seguro. (Imutábilidade)
# Trabalhar com elementos imutáveis traz segurança para o código.

# Copiando uma tupla para outra:
tupla = (1,2,3)
print(f'Tupla 1 {tupla}')
outra = (4,5,6)
nova = tupla + outra


print(f'Tupla Nova {nova}')
print(f'Tupla Outra {outra}')
print(id(tupla)) # ID --> 2245346492096
print(id(outra)) # ID --> 2245346491776
print(id(nova)) # ID --> 2245346007104

"""
