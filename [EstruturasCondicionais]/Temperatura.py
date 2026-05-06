import os
os.system('cls')

temperatura = int(input('Temperatura ambiente atual: '))

if temperatura < 10:
    print('Temperatura Baixa')
elif temperatura >= 10 and temperatura <= 25:
    print('Temperatura Media')
else:
    print('Temperatura Alta')