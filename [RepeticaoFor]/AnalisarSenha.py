import os
os.system('cls')

senha = input('Digite a senha: ')

maiusculas = 0
minusculas = 0
digitos = 0
especiais = 0

for caractere in senha:
    if caractere.isupper():  #Pesquisei essas funções na internet
        maiusculas += 1
    elif caractere.islower():  #Pesquisei essas funções na internet
        minusculas += 1
    elif caractere.isdigit():  #Pesquisei essas funções na internet
        digitos += 1
    else:
        especiais += 1

total = len(senha)

print(f'Quantidade de caracteres: {total}')
print(f'Letras maiusculas: {maiusculas}')
print(f'Letras minusculas: {minusculas}')
print(f'Digitos: {digitos}')
print(f'Caracteres especiais: {especiais}')