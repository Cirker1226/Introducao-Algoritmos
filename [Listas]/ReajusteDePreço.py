lista_original = []
lista_reajuste = []

for i in range(1,9):

    preco = float(input(f'Informe o preço do {i}º produto: '))
    lista_original.append(preco)

    if preco < 100:

        preco = preco + (preco * (10/100))
        lista_reajuste.append(preco)

    elif preco >= 100:

        preco = preco + (preco * (5/100))
        lista_reajuste.append(preco)

lista_original.sort()
lista_reajuste.sort()

print(f'Preços originais: {lista_original}')
print(f'Preços reajustados: {lista_reajuste}')