# Faça um programa que receba dois números inteiros e
# mostre qual o maior deles.
"""
numeros_inteiros = input("Digite dois números inteiros com espaço entre eles: ")
numeros_split = numeros_inteiros.split()

num1 = int(numeros_split[0])
num2 = int(numeros_split[1])

if num1 > num2:
    print(f'O número maior é {num1}')
elif num1 == num2:
    print('Os números são iguais')
else:
    print(f'O número maior é {num2}')
"""

# Faça um programa que leia um número inteiro fornecido pelo usuário.
# Se esse número for positivo, calcule a raiz quadrada do número.
# Se o número for negativo, mostre uma mensagem dizendo que o
# número é invalido.

from math import sqrt

num1 = int(input("Digite um número inteiro: "))

if num1 > 0:
    print(f'A raiz quadrada de {num1} é {sqrt(num1)}')
else:
    print("O número é inválido")


# Faça um programa que receba um número inteiro e informe se ele é
# par ou impar
"""
num1 = int(input("Digite um número inteiro: "))

if num1 % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
"""
