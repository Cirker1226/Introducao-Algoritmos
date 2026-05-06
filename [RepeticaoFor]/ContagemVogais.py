import os
os.system('cls')

palavra = input('Porfavor digite uma palavra: ')

vogais = "aeiouAEIOU"
quantidade = 0

for letra in palavra:
    if letra in vogais:
        quantidade += 1

print(f'A Quantidade de vogais é {quantidade}')