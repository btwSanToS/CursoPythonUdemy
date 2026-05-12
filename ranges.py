"""
- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loop for.

Ranges são utilizados para gerar sequências númericas, não de forma
aleatória, mas sim de maneira especificada.

Formas gerais:

# Forma 1
range(valor_de_parada)
OBS: valor_de_parada não inclusivo (início padrão 0, e passo de 1 em 1)

for num in range(11):
    print(num)

# Forma 2
range(valor_de_inicio, valor_de_parada)
OBS: valor_de_parada não inclusivo (início especificado, e passo de 1 em 1)

for num in range(1, 11):
    print(num)

# Forma 3
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusivo (início especificado, e passo
especificado pelo usuário)

for num in range(5, 50+1, 5):
    print(num)

# Forma 4
range(valor_final, valor_de_inicio, passo)
OBS: valor_de_inicio não inclusivo (valores especificados pelo usuário)

for num in range(10, 0-1, -1):
    print(num)
"""







