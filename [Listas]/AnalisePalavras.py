palavras = []

for i in range(10):
    palavras.append(input('Informe uma Palavra:'))

maior_palavra = palavras[0]
menor_palavra = palavras[0]

quantidade_a = 0
mais_de_5 = []

for palavra in palavras:
    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra

    if len(palavra) < len(menor_palavra):
        menor_palavra = palavra

    if palavra[0] == 'a':
        quantidade_a += 1

    if len(palavra) > 5:
        mais_de_5.append(palavra)

print("Maior palavra:", maior_palavra)
print("Menor palavra:", menor_palavra)
print("Quantidade de palavras que começam com a:", quantidade_a)
print("Palavras com mais de 5 caracteres:", mais_de_5)