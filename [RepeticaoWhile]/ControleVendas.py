import os
os.system ('cls')

valor = float(input('Informe o valor da venda: '))
 
contador = 0
valor_diario = 0
 
while valor != 0:
    valor_diario += valor
    valor = float(input('Informe o valor da venda: '))
 

    contador += 1
 
valor_medio = valor_diario / contador
 
print(f'O valor total de vendas diarias é de R${valor_diario}')
print(f'O valor médio das vendas é de R${valor_medio}')