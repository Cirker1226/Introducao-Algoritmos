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
   
nota = float(input('Digite o valor da nota: '))

resultado = classificar_desempenho(nota)
print(resultado)