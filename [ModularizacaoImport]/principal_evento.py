import funcoes_evento
import os

for i in range(1, 4):
    funcoes_evento.separador()
    print(f'Participante {i}'.center(50))
    funcoes_evento.separador()

    nome = input('Informe o seu nome: ')
    print('Ingressos disponíveis: regular / vip / estudante')
    tipo_ingresso = input('Informe o tipo do ingresso: ')
    valor_padrao = int(input('Informe o valor padrão do ingresso: '))
    oficinas = int(input('Informe a quantidade de oficinas extras: '))
    material_extra = int(input('Informe a quantidade de material extra: '))
    cupom = int(input('Informe um cupom de desconto (%): '))

    valor_base, valor_oficinas, valor_material, valor_desconto, valor_taxa_admin, valor_final, classificacao = funcoes_evento.gerar_relatorio_participante(nome, tipo_ingresso, valor_padrao, oficinas, material_extra, cupom)

    os.system('cls')

    funcoes_evento.separador()
    print('PUC Minas - Evento'.center(50))
    funcoes_evento.separador()

    print(f'Nome: {nome}')
    print(f'Tipo de Ingresso: {tipo_ingresso}')
    print(f'Valor do Ingresso: R$ {valor_base:.2f}')
    print(f'Valor total das oficinas: R$ {valor_oficinas:.2f}')
    print(f'Valor total do material: R$ {valor_material:.2f}')
    print(f'Valor do desconto: R$ {valor_desconto:.2f}')
    print(f'Valor da taxa administrativa: R$ {valor_taxa_admin:.2f}')
    print(f'Valor final da inscrição: R$ {valor_final:.2f}')
    print(f'Classificação: {classificacao}')
    funcoes_evento.separador()