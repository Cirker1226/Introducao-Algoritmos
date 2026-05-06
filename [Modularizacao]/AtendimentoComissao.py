def calcular_comissao(valor_venda):
    comissao = (5/100) * valor_venda
    print(f'O Valor de sua comissão é: {comissao}')

valor_venda = int(input("Digite o valor da venda (R$): "))

calcular_comissao(valor_venda)