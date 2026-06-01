lista = []

for i in range (1,7):

    numero = float(input('Informe um valor númerico: '))

    lista.append(numero)

total = sum(lista)
media = total / i

print(f'Somatorio: {total}')
print(f'Média: {media}')