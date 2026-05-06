import os
os.system('cls' if os.name == 'nt' else 'clear')

quantidade = 5
contador = 1
soma_notas = 0

while contador <= quantidade:
    nota = int(input('Digite o valor da nota: '))
    soma_notas += nota
    contador += 1

media_notas = soma_notas / quantidade

print(f'A média das notas disponibilizadas é: {media_notas}')