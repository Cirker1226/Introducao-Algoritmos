import os
os.system('cls')

idade = int(input('Idade do Usuario: '))
matricula = int(input('Matricula ativa (1 - Sim, 0 - Não): '))
autorizacao_especial = int(input('Autorização Especial (1 - Sim, 0 - Não): '))

if idade >= 18 and matricula == 1:
    print('Acesso Liberado')
elif idade < 18 and autorizacao_especial == 1:
    print('Acesso Liberado')
elif matricula == 0 and autorizacao_especial == 1:
    print('Acesso Liberado')
else:
    print('Acesso Negado')