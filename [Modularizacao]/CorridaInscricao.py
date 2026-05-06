def calcular_inscricao(valor_base, taxa=10):
    valor_novo = valor_base - (valor_base * (taxa/100))
    return valor_novo

valor_base = float(input('Digite o valor base da inscrição: '))

primeiro_resultado = calcular_inscricao(valor_base)

taxa = int(input('Digite o valor da taxa: '))

segundo_resultado = calcular_inscricao(valor_base, taxa)

print(f'Valor com taxa padrão (10%): {primeiro_resultado}')
print(f'Valor com taxa informada ({taxa}%): {segundo_resultado}')