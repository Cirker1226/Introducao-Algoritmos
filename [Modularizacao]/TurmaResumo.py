def classificar_desempenho(nota):
    if nota >= 90 and nota <=100:
        return "Excelente"
    elif nota >= 70 and nota <=89:
        return "Bom"
    elif nota >= 60 and nota <=69:
        return "Regular"
    elif nota >= 0 and nota <=59:
        return "Insuficiente"
    else:
        return "Nota Invalida"
   
def calcular_situacao(nota):
    if nota >= 70 and nota <= 100:
        return 'Aprovado'
    elif nota >= 50 and nota <=69:
        return 'Recuperação'
    elif nota >= 0 and nota <= 49:
        return 'Reprovado'
    else:
        return 'Nota Invalida'

def gerar_resumo_correcao(resultado_situacao, resultado_desempenho):
    print(resultado_desempenho)
    print(resultado_situacao)

nota = float(input('Digite o valor da nota: '))

desempenho = classificar_desempenho(nota)
situacao = calcular_situacao(nota)

gerar_resumo_correcao(desempenho, situacao)