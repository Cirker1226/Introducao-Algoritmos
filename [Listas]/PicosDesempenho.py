treinos = []

for i in range(10):
    pontos = float(input('Pontuação do Treino: '))
    treinos.append(pontos)

posicoes_picos = []
valores_picos = []

for i in range(1, len(treinos) - 1):
    if treinos[i] > treinos[i - 1] and treinos[i] > treinos[i + 1]:
        posicoes_picos.append(i)
        valores_picos.append(treinos[i])

print("Quantidade de picos:", len(posicoes_picos))
print("Posições dos picos:", posicoes_picos)
print("Valores dos picos:", valores_picos)