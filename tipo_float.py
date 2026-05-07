"""
Tipo Float (Tipo real, decimal)
--> Casas Decimais
OBS:
O separador de casas decimais na programação é ponto, não vírgula;

Maneira incorreta:
Valor = 1,44
Maneira correta:
Valor = 1.44
"""

# Atribuição dupla:
valor1, valor2 = 1, 44
print(valor1)
print(valor2)

# Mudança de tipo
"""
OBS:
Ao converter valores float para inteiros, nós perdemos precisão.
"""
valor = 1.44
res = int(valor)
print(res)

# Trabalhando com números complexos deve-se inserir 'j' ao número
valor_complexo = 5j
print(type(valor_complexo))
