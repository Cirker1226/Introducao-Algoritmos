numeros = []

for i in range(12):
    numeros.append(int(input('Informe um valor númerico inteiro: ')))

maior_sequencia = 1
sequencia_atual = 1

for i in range(1, len(numeros)):
    if numeros[i] > numeros[i - 1]:
        sequencia_atual += 1
    else:
        if sequencia_atual > maior_sequencia:
            maior_sequencia = sequencia_atual
        sequencia_atual = 1

if sequencia_atual > maior_sequencia:
    maior_sequencia = sequencia_atual

print("Maior sequência crescente:", maior_sequencia)