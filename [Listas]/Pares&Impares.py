pares = 0
impares = 0

lista_pares = []
lista_impares = []

for i in range(0, 10):
    numero = int(input('Informe um valor númerico inteiro: '))

    if numero % 2 == 0:
        pares += 1
        lista_pares.append(numero)

    else:
        impares += 1
        lista_impares.append(numero)

print(f'Quantidade de Pares: {pares}')
print(f'Quantidade de Impares: {impares}')
print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')
