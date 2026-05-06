import funcoes_cafeteria
import os

nome = input('Informe o produto: ')
valor_base = int(input('Informe o valor do produto: '))
acrescimo = int(input('Informe o acrescimo do tamanho do café: '))
acompanhamento = input('Informe o nome do acompanhamento: ')
valor_acompanhamento = int(input('Informe o valor do acompanhamento: '))
desconto_acompanhamento = int(input('Informe a % de desconto do produto: '))
taxa_servico = int(input('Informe a % da taxa de servico: '))

os.system('cls')

preco_cafe = funcoes_cafeteria.calcular_preco_cafe(valor_base, acrescimo)
preco_acomp = funcoes_cafeteria.calcular_acompanhamento(valor_acompanhamento, desconto_acompanhamento)

preco_cafe = funcoes_cafeteria.calcular_preco_cafe(valor_base, acrescimo)
preco_acomp = funcoes_cafeteria.calcular_acompanhamento(valor_acompanhamento, desconto_acompanhamento)


subtotal, taxa, total = funcoes_cafeteria.calcular_totais(preco_cafe, preco_acomp, taxa_servico)

funcoes_cafeteria.separador()
print('Cafeteria PUC MINAS'.center(50))
funcoes_cafeteria.separador()
funcoes_cafeteria.resumo_item(nome, preco_cafe)
funcoes_cafeteria.resumo_item(acompanhamento, preco_acomp)

funcoes_cafeteria.separador()
print(f'Subtotal: R${subtotal:.2f}')
print(f'Taxa de serviço: R${taxa:.2f}')
print(f'Total: R${total:.2f}')
funcoes_cafeteria.separador()