"""
Módulo Collections: Ordered Dict.

-- Em um dicionário, a ordem de inserção dos elementos não é garantida.
Já com o Ordered Dict, a ordem será mantida. 

OrderedDict é um dicionário que nos garante a ordem de inserção dos 
elementos.

"""

from collections import OrderedDict
dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave} valor={valor}')