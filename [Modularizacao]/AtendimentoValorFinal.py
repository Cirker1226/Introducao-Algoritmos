def calcular_valor_final(valor_produto, desconto):
    valor_final = valor_produto - (valor_produto * (desconto/100))
    print(f'O valor final do produto é: {valor_final}')
   
valor_produto = int(input('Digite o valor do produto: '))
desconto = int(input('Digite o percentual de desconto: '))

calcular_valor_final(valor_produto, desconto)