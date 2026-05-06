def separador():
    print('-'*50)

def cabeçalho(nome_da_loja):
    print(nome_da_loja.center(50))

def cliente(nome_do_cliente):
    print(f'Cliente: {nome_do_cliente}')

def valor_produto(valor_original):
    print(f'Valor Original: R${valor_original}')

def percentual(desconto):
    print(f'Percentual de Desconto: {desconto}%')

def valor_final(valor_original, desconto):
    valor_final = valor_original - (valor_original * (desconto/100))
    print(f'Valor final: R${valor_final}')

def comissao(valor_final):
    comissao = valor_final * (5/100)
    print(f'Comissão: R${comissao}')


def sistema(nome_da_loja, nome_do_cliente, valor_original, desconto):
    separador()
    cabeçalho(nome_da_loja)
    separador()
    cliente(nome_do_cliente)
    valor_produto(valor_original)
    percentual(desconto)
    valor_final(valor_original, desconto)
    separador()
   
nome_da_loja = input('Informe o nome da Loja: ')
nome_do_cliente = input('Informe o nome do cliente: ')
valor_original = float(input('Informe o valor do produto: '))
desconto = int(input('Informe o percentual de desconto: '))

sistema(nome_da_loja, nome_do_cliente, valor_original, desconto)