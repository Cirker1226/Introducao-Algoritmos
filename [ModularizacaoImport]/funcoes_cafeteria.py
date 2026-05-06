def separador():
    print('-'*50)


def calcular_preco_cafe(preco_base, acrescimo=0):
    preco_produto = preco_base + acrescimo


    return preco_produto


def calcular_acompanhamento(preco, desconto=0):
    preco_acompanhamento = preco + (preco * (desconto/100))


    return preco_acompanhamento


def resumo_item(nome, valor):
    print(f'{nome} - R${valor}')


def calcular_totais(valor1, valor2, taxa_servico=10):
    somatorio = valor1 + valor2
    taxa = somatorio * (taxa_servico/100)
    valor_total = somatorio + taxa


    return somatorio, taxa, valor_total