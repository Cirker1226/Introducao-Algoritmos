import os
os.system ('cls')
 
linhas = int(input('Digite o número de linhas: '))
colunas = int(input('Digite o número de colunas: '))
 
contador = 0
 
while contador < linhas:
    i = 0
    while i < colunas:
        print('*', end="")
        i += 1
    print()
    contador += 1