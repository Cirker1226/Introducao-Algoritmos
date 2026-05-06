import os
os.system('cls')

numero = int(input("Digite um número inteiro positivo: "))

contador = 1
soma = 0

while contador <= numero:
    soma += contador
    contador += 1

print(f"A soma de todos os numeros de 1 até {numero} é: {soma}")