import os
os.system('cls')

palavra = input('Digite uma palavra: ')
caractere = input('Digite um caractere (!/@): ')

quantidade = 0

for letra in palavra:
    if letra in caractere:
        quantidade += 1

print(f'A quantidade de caracteres na palavra é: {quantidade}')