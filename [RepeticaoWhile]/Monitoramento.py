import os
os.system ('cls')              
 
temperatura = int(input('Temperatura Registrada:'))
 
contador = 0
soma = 0
 
maior = temperatura
menor = temperatura
 
while temperatura != -1:
    soma += temperatura

    contador += 1
 
    if temperatura > maior:
        maior = temperatura
    if temperatura < menor:
        menor = temperatura
 
    temperatura = int(input('Temperatura Registrada:'))

media = soma / contador

print(f'A média das temperaturas registradas são {media}')
print(f'A menor temperatura registrada foi {menor} e a maior foi {maior}')