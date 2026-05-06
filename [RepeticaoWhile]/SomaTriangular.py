import os
os.system ('cls')

numero = int(input("Digite um número inteiro positivo: "))

contador = 1
denominador = 1
soma = 0

while contador <= numero:
    soma = soma + (contador/denominador)
    contador = contador + 1
    denominador = denominador + contador

print(f"Série: {soma}")