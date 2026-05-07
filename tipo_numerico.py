"""
Tipo Númerico
{1} -- Duas barras // transformará o resultado em Inteiro;
{2} -- Duas asteriscos ** será elevado;
{3} -- Porcentagem % será o resto da divisão. Importante para
descobrir se o valor é Par(0) ou Ímpar(1);
{4} -- É possível saber as casas decimais inserindo Underline(_)
no valor. Ex: 1000000000 --> 1_000_000_000;
{5} -- Incrementos (+=, -=, *=, /=);
{6} -- Utilizar type('variavel') para saber o Tipo da variável.
"""

num1 = 5
num2 = 2
def calcular():
    return num1//num2
print(calcular())