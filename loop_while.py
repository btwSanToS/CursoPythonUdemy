"""
Loop while
Utilizar o while quando não souber quantas vezes o código irá se repetir.
Forma geral:
While expressão booleana:
    // Execução do loop

contador = 1
while contador <= 5:
    print(contador)
    contador += 1

numero = input("Digite um número: ")

while not numero.isdigit():
    print("Você deve digitar um número")
    numero = input("Digite um número: ")

numero = int(numero)
print(f'O número digitado foi {numero}')

# While com soma
qntd = int(input('Quantos números deseja somar? '))

contador = 1
soma = 0

while contador <= qntd:
    numero = input(f'Digite o número {contador}: ')
    soma += int(numero)
    contador += 1

print(soma)

"""



# While True

while True:
    comando = input("Digite 'sair' para encerrar: ")

    if comando == 'sair':
        print("Usuário deslogado com sucesso")
        break

    print(f"Você digitou '{comando}'")



