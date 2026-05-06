import os
os.system('cls')

palavra = input("Porfavor, digite uma palavra: ")

eh_palindromo = True

for letra in range(len(palavra)):
    if palavra[letra] != palavra[-letra -1]:
        eh_palindromo = False

if eh_palindromo:
    print('A Palavra é um palindromo')
else:
    print('A Palavra não é um palindromo')