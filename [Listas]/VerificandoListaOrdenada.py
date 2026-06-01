lista = []

for i in range(8):
    numero = int(input('Digite um valor númerico inteiro: '))

    lista.append(numero)

ordenada = lista.copy()
lista.sort()

if lista == ordenada:
    print('A lista está em ordem crescente.')
else:
    print('A lista não está em ordem crescente.')