"""
Escopo de variáveis

Dois casos de escopo:
[1] -- Variáveis globais:
        - Seu escopo compreende todo o programa;
[2] -- Variáveis locais:
        - São reconhecidas somente no bloco onde foram declaradas;
Para declarar variáveis em Python, fazemos, em snake_case:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica.
Isso significa que ao declarar a variável, não é preciso colocar o tipo dela.
Este tipo é inferido ao atribuírmos o valor à mesma

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;

Já em Python, não é necessário declarar a tipagem
"""
num1 = 5 # Variável global
num2 = 40.5 # Variável global
print(num1, num2)
print(type(num1))
#int
print(type(num2))
#float

# Reatribuição de variável em Python.
# Colocar novamente uma varíavel declarada, mas com outra tipagem

#num1 = 'gouki final boss' # Variável global
print(type(num1))
#str

novo = 0

if num1 > 10:
    novo = num1 + 10
    print(novo)
# Caso a variável esteja em um escopo Local, ao tentar acessar, irá quebrar.
# Para isso, pode ser possível declarar a mesma com valor 0, null, branco, etc.
print(novo)