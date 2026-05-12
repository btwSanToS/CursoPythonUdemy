"""
Faça um programa que determine e mostre os cinco primeiros múltiplos
 de 3, considerando números maiores que 0

num = 1
contador = 0

while contador < 5:
    if num % 3 == 0:
        print(num)
        contador += 1
    num += 1
"""

"""
Faça um programa que utilize o comando while para mostrar na tela uma 
contagem regressiva, iniciando em 10 e terminando em 0.
Mostre também uma mensagem "FIM!" após a contagem.

inicio = 10

while inicio > -1:
    print(inicio)
    inicio -= 1
    
print("FIM!")
"""

"""
Faça um programa que declare um inteiro, inicialize-o em 0, incremente-o
de 1000 em 1000, imprimindo seu valor na tela, até que seu valor seja 
100.000 (cem mil)

num = int(input("Digite um valor inteiro: "))

while num < 100_000:
    num += 1_000


    if num > 100_000:
        num = 100_000
        
    print(num)
"""
