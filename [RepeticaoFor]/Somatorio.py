import os
os.system('cls')

n = int(input('Digite um número: '))
m = int(input('Digite um número maior que o anterior: '))

while m < n:
    m = int(input('ERRO! Porfavor digite um número maior que o anterior: '))

soma = 0

for numero in range (n, m + 1):
    soma += numero

print(f'O resultado final é {soma}')