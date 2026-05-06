import os
os.system ('cls')
 
numero = int(input('Digite um valor númerico inteiro: '))
 
maior = numero
menor = numero

contador = 1

while contador < 8:
    numero = int(input('Digite um valor númerico inteiro: '))
 
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
 
    contador += 1
 
print(f'Seu maior número é: {maior} enquanto seu menor número é: {menor}')