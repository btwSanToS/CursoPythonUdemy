"""
Módulo Collectinos - Default Dict

defaultdict é uma variação do dic comum (Dicionário).

A diferença é que, quando acessamos uma chave inexistente, ele cria 
automaticamente um valor padrão para essa chave.

Exemplos:
    defaultdict(int) -> valor padrão 0
    defaultdict(list) -> valor padrão []
    defaultdict(set) -> valor padrão set()
    defaultdict(lambda: 'valor') -> valor padrão personalizado

É muitop útil para:
    contar elementos;
    agrupar dados;
    evitar key error;
    simplificar código com dicionário.
    
dicionario = {}
# print(dicionario['nome']) #KeyError: 'nome'

contador = defaultdict(int)
contador['python'] += 1
contador['javascript'] += 1
contador['python'] += 1
print(contador)


alunos_por_curso = defaultdict(list)
alunos_por_curso['Python'].append('Ana')
alunos_por_curso['Python'].append('Diogo')
alunos_por_curso['Javascript'].append('André')
print(alunos_por_curso)

linguagens_por_aluno = defaultdict(set)
linguagens_por_aluno['Ana'].add('Python')
linguagens_por_aluno['Ana'].add('Javascript')
linguagens_por_aluno['Ana'].add('C#')

print(linguagens_por_aluno)

"""
from collections import defaultdict

linguagens_por_aluno = defaultdict(set)
linguagens_por_aluno['Ana'].add('Python')
linguagens_por_aluno['Ana'].add('Javascript')
linguagens_por_aluno['Ana'].add('C#')

print(linguagens_por_aluno)
