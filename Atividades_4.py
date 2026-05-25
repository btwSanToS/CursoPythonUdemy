"""
from collections import Counter

Transforme o texto em uma lista de palavras.
Use Counter para contar quantas vezes cada palavra aparece.
Mostre as 3 palavras mais usadas.

texto = 
python é bom para dados
python é bom para automação
dados com python são muito úteis
automação com python economiza tempo

counter_texto = Counter(texto.lower().split())
print(counter_texto.most_common(3))

////////////////////////////////////////////////////////////////

Conte quantas vezes cada produto foi vendido.
Mostre o produto mais vendido.
Mostre os dois produtos mais vendidos.
Acesse diretamente quantas vezes 'mouse' foi vendido.

vendas = [
    'notebook',
    'mouse',
    'teclado',
    'notebook',
    'mouse',
    'notebook',
    'monitor',
    'teclado',
    'mouse',
    'notebook'
]

counter_vendas = Counter(vendas)
print(counter_vendas)
print(counter_vendas.most_common(1))
print(counter_vendas.most_common(2))
print(counter_vendas['mouse'])

////////////////////////////////////////////////////////////////

from collections import defaultdict

Crie um defaultdict(list).
Agrupe os alunos por curso.
O resultado final deve ficar parecido com:

alunos = [
    ('Ana', 'Python'),
    ('Carlos', 'JavaScript'),
    ('João', 'Python'),
    ('Marcos', 'Python'),
    ('Pedro', 'JavaScript'),
    ('Lucas', 'Java')
]

alunos = defaultdict(list)
alunos['Python'].append('Ana')
alunos['Javascript'].append('Carlos')
alunos['Python'].append('João')
alunos['Python'].append('Marcos')
alunos['Javascript'].append('Pedro')
alunos['Java'].append('Lucas')

print(alunos)


////////////////////////////////////////////////////////////////

Crie um defaultdict(int).
Conte quantas vezes cada status aparece.
Mostre o resultado final.
Mostre quantos pedidos estão com status 'pago'.

status_pedidos = defaultdict(int)
status_pedidos ['pago'] += 1
status_pedidos ['pendente'] += 1
status_pedidos ['pago'] += 1
status_pedidos ['cancelado'] += 1
status_pedidos ['pago'] += 1
status_pedidos ['pendente'] += 1
status_pedidos ['cancelado'] += 1
status_pedidos ['pago'] += 1

print(status_pedidos)



////////////////////////////////////////////////////
Corrigindo:

alunos = [
    ('Ana', 'Python'),
    ('Carlos', 'JavaScript'),
    ('João', 'Python'),
    ('Marcos', 'Python'),
    ('Pedro', 'JavaScript'),
    ('Lucas', 'Java')
]

alunos_por_cursos = defaultdict(list)
for aluno, curso in alunos:
    alunos_por_cursos[curso].append(aluno)
print(alunos_por_cursos)

"""


from collections import defaultdict

pedidos = [
    'pago',
    'pendente',
    'pago',
    'cancelado',
    'pago',
    'pendente',
    'cancelado',
    'pago'
]

status_do_pedido = defaultdict(int)
for status in pedidos:
    status_do_pedido[status] +=1
print(status_do_pedido)
print(status_do_pedido['pago'])
