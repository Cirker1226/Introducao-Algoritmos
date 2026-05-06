import os
os.system('cls')

nota = int(input('Digite a nota do aluno (0 a 100): '))

if nota >= 90:
    print('Excelente')
elif nota >= 70 and nota <= 89:
    print('Bom')
elif nota >= 50 and nota <=69:
    print('Regular')
else:
    print('Insuficiente')