lista_nomes = []
quantidade = 0

for i in range (8):
    nome = input('Digite um nome: ')
    lista_nomes.append(nome)

nome_encontrado = input('Informe o nome a ser encontrado: ')

for palavra in lista_nomes:

    if palavra == nome_encontrado:
        quantidade += 1

if quantidade > 0:
    print('Nome encontrado.')
else:
    print('Nome não encontrado.')

print(f'Quantidade de ocorrências: {quantidade}')