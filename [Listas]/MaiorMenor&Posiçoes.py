lista = []

posicao_menor = 0
posicao_maior = 0

for i in range(7):

    numeros = int(input('Informe um valor númerico inteiro: '))
    lista.append(numeros)

maior = lista[0]
menor = lista[0]

for numero in range (1, len(lista)):

    if lista[numero] > maior:

        maior = lista[numero]
        posicao_maior = numero

    if lista[numero] < menor:

        menor = lista[numero]
        posicao_menor = numero

print(f'Maior valor: {maior}')
print(f'Posição do maior valor: {posicao_maior}')
print(f'Menor valor: {menor}')
print(f'Posição do menor valor: {posicao_menor}')