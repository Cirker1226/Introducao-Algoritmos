import os
os.system('cls')
 
numero = int(input('Digite um valor númerico positivo: '))
 
contador = 1
 
while contador <= 10:
    multiplicacao = numero * contador
    print(f'{numero} x {contador} = {multiplicacao}')
    contador += 1