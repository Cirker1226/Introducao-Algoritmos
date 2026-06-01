lista_temperatura = []

aumentou = 0
diminuiu = 0
igual = 0

for i in range(10):

    temperatura = float(input('Informe a temperatura: '))
    lista_temperatura.append(temperatura)

for temperatura in range(1, len(lista_temperatura)):

    if lista_temperatura[temperatura] > lista_temperatura[temperatura - 1]:
        aumentou += 1

    elif lista_temperatura[temperatura] < lista_temperatura[temperatura - 1]:
        diminuiu += 1

    else:
        igual += 1

print(f'Aumentou: {aumentou} Vezes')
print(f'Diminuiu: {diminuiu} Vezes')
print(f'Igual: {igual} Vezes')