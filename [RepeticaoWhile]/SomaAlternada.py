import os
os.system ('cls')

numero = int(input("Digite um número inteiro positivo: "))

contador = 1
soma = 0
sinal = 1

while contador <= numero:
    soma = soma + sinal * (1/contador)
    sinal = sinal * -1
    contador += 1

print(f"Serie = {soma}")