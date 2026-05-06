import os
os.system('cls')
 
contador = 1
 
pares = 0
impares = 0
 
while contador <= 10:
    numero = int(input('Digite o valor a ser analizado: '))
    contador += 1
 
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
 
print(f'Quantidades de numeros Pares: {pares}')
print(f'Quantidades de numeros Impares: {impares}')