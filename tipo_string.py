"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:
-- Estiver em àspas simples -> 'x'
-- Estiver em àspas duplas -> "xxx"
-- Estiver em àspas simples triplas -> '''xxx'''
"""
#- Estiver em àspas duplas triplas -> """xxx"""
nome = 'Geek University'
print(nome)
print(type(nome))

# O mais comum de ser utilizado é àspas simples
# Ex nome com àspas:

nome1 = "Gina's Bar"
print(nome1)
print(type(nome1))

# Quebra de linha: \n
nome2 = 'Angelina \nJolie'
print(nome2)

nome3 = 'Geek University'
print(nome3.upper())
# Todas as letras maiúscula

nome4 = 'Geek University'
print(nome4.lower())
# Todas as letras minúscula

nome5 = 'Geek University Estudo'
print(nome5.split())
# Transforma em uma lista de strings

print(nome5[0:6]) # Slice de string
print(nome5[5:13]) # Slice de string

print(nome5.split()[0])
print(nome5.split()[1])

# Invertendo a string
print(nome5[::-1])
"""
[::-1] -> Comece do primeiro elemento, vá até o último elemento 
e inverta
"""
