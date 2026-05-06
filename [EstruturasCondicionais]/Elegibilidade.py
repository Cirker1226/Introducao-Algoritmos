import os
os.system('cls')

idade = int(input('Digite a idade do cliente: '))
valor_compra = float(input('Digite o valor da compra: '))

if idade >= 60 or valor_compra > 200:
    print('Cliente elegivel para desconto')
else:
    print('Cliente sem desconto')