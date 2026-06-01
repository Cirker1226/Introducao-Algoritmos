lista = []

lista_media = []
acima_media = 0

for i in range(1, 11):

    nota = float(input('Informe o valor da nota obtida: '))
    lista.append(nota)

    if nota > 60:
        acima_media += 1
        lista_media.append(nota)

total = sum(lista)
media = total / i

print(f'Média da turma: {media}')
print(f'Quantidade acima da media: {acima_media}')
print(f'Notas acima da media: {lista_media}')
