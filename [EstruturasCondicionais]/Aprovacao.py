import os
os.system('cls')

media = int(input('Média final do aluno: '))
frequencia = int(input('Percentual de Frequencia do Aluno: '))

if frequencia < 75:
    print('Reprovado por excesso de faltas.')
elif media >= 60:
    print('Aprovado')
elif media >=40 and media <= 59:
    print('Recuperação')
else:
    print('Reprovado por Nota')