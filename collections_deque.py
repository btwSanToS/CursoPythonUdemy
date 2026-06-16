"""
Módulo Collectinos - Deque

Podemos dizer que o deque é uma lista de alta performance.
"""
from collections import deque

# Criando Deques:
deq1 = deque('Geek')
print(deq1)

# Adicionando elementos no deque
deq1.append('y') # Adiciona ao final da Deque
print(deq1)

deq1.appendleft('--') # Adiciona ao início da Deque
print(deq1)

deq1.pop() # -- Remove ao final do Deque
print(deq1)

deq1.popleft() # -- Remove ao início do Deque
print(deq1)