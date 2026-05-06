import os
os.system('cls')

numero = int(input('Digite um número inteiro positivo: '))

for linha in range(numero):
    for coluna in range(numero):
        if linha == 0 or linha == numero - 1 or coluna == 0 or coluna == numero - 1:
            print('1', end='')
        else:
            print('0', end='')
    print()