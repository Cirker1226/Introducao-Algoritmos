def divisoria():
    print('-'*30)

def exibir_nome(nome):
    print(nome)

def calcular_inscricao(valor_base, taxa=10):
    valor_novo = valor_base - (valor_base * (taxa/100))
    return valor_novo

def converter_tempo(total_segundos):
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60
    return horas, minutos, segundos

def gerar_resumo_tempo(total_segundos):
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60
    return horas, minutos, segundos

def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def contar_pares_faixa(inicio, fim):
    contador = 0
    for numero in range(inicio, fim):
        if eh_par(numero):
            contador += 1
    return contador

def exibir_fechamento(nome, valor_base, total_segundos, inicio, fim):
    divisoria()
    exibir_nome(nome)
    divisoria()

    valor_com_desconto = calcular_inscricao(valor_base, taxa=10)
    print(f'Valor da inscrição com desconto: R$ {valor_com_desconto:.2f}')

    horas, minutos, segundos = converter_tempo(total_segundos)
    print(f'Tempo de prova: {horas}h {minutos}min {segundos}s')

    total_pares = contar_pares_faixa(inicio, fim)
    print(f'Pares entre {inicio} e {fim}: {total_pares}')

    divisoria()


nome = input('Informe o nome do participante: ')
valor_base = float(input('Informe o valor da inscrição: '))
total_segundos = int(input('Informe o tempo levado em segundos: '))
inicio = int(input('Informe o valor inicial a ser analisado: '))
fim = int(input('Informe o valor final a ser analisado: '))

exibir_fechamento(nome, valor_base, total_segundos, inicio, fim)