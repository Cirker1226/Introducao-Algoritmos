def calcular_situacao(nota):
    if nota >= 70:
        return 'Aprovado'
    elif nota >= 50 and nota <=69:
        return 'Recuperação'
    else:
        return 'Reprovado'
   
nota = float(input('Digite o valor da nota: '))

resultado = calcular_situacao(nota)
print(resultado)