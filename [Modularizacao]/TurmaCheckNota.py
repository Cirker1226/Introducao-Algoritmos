def verificacao_nota(nota):
    if nota >= 0 and nota <= 100:
        return True
    else:
        return False

nota = float(input('Digite o valor da nota: '))

resultado = verificacao_nota(nota)
print(resultado)    