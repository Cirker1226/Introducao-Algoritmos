import os
os.system ('cls')
numero = int(input("Digite um número inteiro positivo: "))

contador = 1
soma = 0

while contador <= numero:
    soma = soma + (1/contador)
    contador += 1

print(f"Serie = {soma}")