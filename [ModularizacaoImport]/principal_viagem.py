import funcoes_viagem
import os

passagem = float(input('Informe o valor da passagem: '))
bagagem = float(input('Informe o valor da taxa da bagagem: '))
valor_diaria = float(input('Informe o valor da diaria: '))
dias = int(input('Informe a quantidade de dias da diaria: '))
taxa_extra = float(input('Informe o valor da taxa opcional da hospedagem: '))
total_horas = int(input('Informe a duração da viagem (Em horas): '))
alimentacao = float(input('Informe o valor do gasto com alimentação: '))

os.system('cls')

valor_final_passagem = funcoes_viagem.calcular_passagem(passagem, bagagem)
valor_final_hospedagem = funcoes_viagem.calcular_hospedagem(valor_diaria, dias, taxa_extra)
duracao_dias, duracao_horas = funcoes_viagem.converter_duracao(total_horas)

custo_fixo, custo_extra, custo_total = funcoes_viagem.calcular_orcamento(valor_final_passagem, valor_final_hospedagem, alimentacao)

funcoes_viagem.separador()
print('PUC Minas - Agencia'.center(50))
funcoes_viagem.separador()

print(f'Passagem: R${valor_final_passagem}')
print(f'Hospedagem: R${valor_final_hospedagem}')
print(f'Duração: {duracao_dias} dias e {duracao_horas} horas')
print(f'Custo Fixo: R${custo_fixo}')
print(f'Custo Extra: R${custo_extra}')
print(f'Custo Total: R${custo_total}')

funcoes_viagem.separador()