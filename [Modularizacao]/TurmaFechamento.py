def validacao_nota(nota):
    if nota >= 0 and nota <= 100:
        return 'Valida'
    else:
        return 'Invalida'

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
   
def exibir_informacoes(nome,nota,validade,situacao,desempenho):
    print(f'Nome do Aluno: {nome}')
    print(f'Nota Informada: {nota}')
    print(f'Validação da Nota: {validade}')
    print(f'Situacao do Aluno: {situacao}')
    print(f'Desempenho do Aluno: {desempenho}')

for i in range(3):
    nome = input('Digite o nome do aluno: ')
    nota = float(input('Digite o valor da nota: '))

    validade = validacao_nota(nota)
    desempenho = classificar_desempenho(nota)
    situacao = calcular_situacao(nota)

    exibir_informacoes(nome,nota,validade,situacao,desempenho)