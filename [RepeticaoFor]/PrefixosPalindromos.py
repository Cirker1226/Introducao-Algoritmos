import os
os.system('cls')

palavra = input('Digite uma palavra: ')

for tamanho in range(1, len(palavra) + 1):
    prefixo = ''
    for i in range(tamanho):
        prefixo += palavra[i]

    invertido = ''
    for i in range(tamanho - 1, -1, -1):
        invertido += prefixo[i]

    if prefixo == invertido:
        print(f'"{prefixo}" é palindromo')