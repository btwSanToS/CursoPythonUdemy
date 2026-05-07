"""
Recebendo dados do usuário
"""
"""
# Entrada de dados
print("Qual o seu nome?")
nome = input().title() #Input -> Entrada
#Ex print antigo:
#print('Seja bem-vindo(a) %s!' % nome)
#Ex print moderno v1:
#print('Seja bem-vindo(a) {0}'.format(nome))
#Ex print moderno atual:
print(f'Seja bem-vindo {nome}!')
print("Qual a sua idade?")
idade = int(input())
#Já utilizar o cast na variável, para não poluir o print.

# Processamento

# Saída de dados
#Ex print antigo:
#print('%s tem %s anos!' % (nome, idade))
#Ex print antigo:
#print('{0} tem {1} anos!'.format(nome,idade))
print(f'{nome} tem {idade} anos!')
print(f'{nome} nasceu em {2026 - idade}!')
"""

#Melhor forma de escrita:
nome = input("Qual o seu nome? ").title()
print(f'Seja bem-vindo {nome}')
idade = int(input("Qual a sua idade? "))
print(f'{nome} tem {idade} anos!')
print(f'{nome} nasceu em {2026 - idade}!')