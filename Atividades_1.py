# Faça um programa que leia um número inteiro e imprima-o.
"""
num1 = input("Insira um número inteiro: ")
if num1.isdigit():
    num1 = int(num1)
    print(f'O número {num1} é inteiro!')
else:
    print(f'O número {num1} não é inteiro!')
"""
from wsgiref.validate import validator

# Faça um programa que peça para o usuário digitar 3 valores inteiros
# e imprima a soma deles.
""" Forma simples:
print("Digite 3 números inteiros: ")
num2 = int(input(""))
num3 = int(input(""))
num4 = int(input(""))
soma = num2 + num3 + num4
print(f"A soma dos valores é {soma}")
"""

""" Versão complexa:
num_digitados = input("Digite 3 números inteiros separados por espaço: ")
num_split = num_digitados.split()

if len(num_split) == 3:
    validator = num_split[0].isdigit() and num_split[1].isdigit() and num_split[2].isdigit()
    if validator:
        num1 = int(num_split[0])
        num2 = int(num_split[1])
        num3 = int(num_split[2])

        soma = num1 + num2 + num3
        print(f"A soma dos valores é {soma}")
else:
    print("Você deve digitar exatamente 3 números.")
"""

# Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores
# lidos.


num_digitados = input("Digite 3 números separados por espaço: ")
num_split = num_digitados.split()

if len(num_split) == 3:
    validator = num_split[0].isdigit() and num_split[1].isdigit() and num_split[2].isdigit()
    if validator:
        num1 = int(num_split[0]) ** 2
        num2 = int(num_split[1]) ** 2
        num3 = int(num_split[2]) ** 2

        soma = num1 + num2 + num3
        print(f"A soma dos quadrados é {soma}")
    else:
        print("Você deve digitar somente números.")
else:
    print("Você deve digitar exatamente 3 números.")






