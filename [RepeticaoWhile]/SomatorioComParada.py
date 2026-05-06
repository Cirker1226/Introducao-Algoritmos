import os
os.system('cls')

numero_desejado = int(input('Digite um valor númerico inteiro: '))

soma = 0
contador = 0

while numero_desejado != 0:
    soma += numero_desejado
    numero_desejado = int(input('Digite um valor númerico inteiro: '))
    contador += 1
    
print(f'O resultado final da soma de todos os numeros informados é: {soma}')