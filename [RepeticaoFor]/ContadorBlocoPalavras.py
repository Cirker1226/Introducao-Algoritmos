import os
os.system('cls')

texto = input('Digite o texto: ')
 
contador = 0
dentro_de_palavra = False
 
for caractere in texto:
    if caractere != ' ' and not dentro_de_palavra:
        contador += 1
        dentro_de_palavra = True
    elif caractere == ' ':
        dentro_de_palavra = False
 
print(f'Quantidade de palavras: {contador}')