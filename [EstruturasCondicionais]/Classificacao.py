import os
os.system('cls')

pontuação = float(input('Digite a pontuação do participante: '))
tempo_total = int(input('Digite o tempo total gasto(em minutos): '))

if pontuação >= 90 and tempo_total < 120:
    print('Classificação: Ouro - Participante destaque da competição')
elif pontuação >= 90:
    print('Classificação: Ouro')
elif pontuação >=70:
    print('Classificação: Prata')
elif pontuação >= 50:
    print('Classficiação: Bronze')
else:
    print('Sem medalha aplicavel')