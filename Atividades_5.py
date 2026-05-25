from collections import defaultdict, Counter
"""
Crie um defaultdict(int) para contar quantos produtos existem 
por categoria.

produtos = [
    ('Notebook', 'Eletrônicos'),
    ('Mouse', 'Eletrônicos'),
    ('Cadeira', 'Móveis'),
    ('Mesa', 'Móveis'),
    ('Teclado', 'Eletrônicos'),
    ('Caneta', 'Papelaria'),
    ('Caderno', 'Papelaria'),
    ('Monitor', 'Eletrônicos')
]

categoria_produtos = defaultdict(int)
for produto, categoria in produtos:
    categoria_produtos[categoria] += 1
print(categoria_produtos)

/////////////////////////////////////////

produtos = [
    ('Notebook', 'Eletrônicos'),
    ('Mouse', 'Eletrônicos'),
    ('Cadeira', 'Móveis'),
    ('Mesa', 'Móveis'),
    ('Teclado', 'Eletrônicos'),
    ('Caneta', 'Papelaria'),
    ('Caderno', 'Papelaria'),
    ('Monitor', 'Eletrônicos')
]

categoria_produtos = defaultdict(list)
for produto, categoria in produtos:
    categoria_produtos[categoria].append(produto)
print(categoria_produtos)


////////////////////////////////////////////

tarefas = [
    ('Criar tela de login', 'feito'),
    ('Criar dashboard', 'pendente'),
    ('Corrigir bug do menu', 'feito'),
    ('Criar API de usuários', 'em andamento'),
    ('Ajustar layout mobile', 'pendente'),
    ('Configurar banco', 'feito'),
    ('Criar testes', 'em andamento')
]

status_tarefas = defaultdict(int)
for tarefa, status in tarefas:
    status_tarefas[status] +=1
print(status_tarefas)

//////////////////////////////////////////

tecnologias = [
    'Python',
    'JavaScript',
    'Python',
    'SQL',
    'Python',
    'JavaScript',
    'Django',
    'SQL',
    'Python',
    'Django',
    'React'
]

counter_tecnologia = Counter(tecnologias)
print(counter_tecnologia)
print(counter_tecnologia.most_common(2))
print(counter_tecnologia['Python'])

"""
