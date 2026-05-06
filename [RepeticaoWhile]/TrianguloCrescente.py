import os
os.system ('cls')

numero = int(input('Digite um número inteiro possitvo: '))

linha = 1
 
while linha <= numero:
    coluna = 1
    while coluna <= linha:
        print(coluna, end="")
        coluna += 1
    print()
    linha += 1