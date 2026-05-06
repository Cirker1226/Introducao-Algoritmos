import funcoes_treino
import os

calorias_base = float(input("Informe a quantidade base de calorias: "))
bonus_calorias = float(input("Informe o bonus de calorias: "))
tempo = int(input("Informe o tempo total gasto (Min): "))
aquecimento = int(input("Informe o tempo de aquecimento (Min): "))
meta_semanal = float(input("Informe a meta semanal: "))

calorias_totais = funcoes_treino.calcular_calorias(calorias_base, bonus_calorias)
tempo_total = funcoes_treino.calcular_tempo_treino(tempo, aquecimento)
horas, minutos = funcoes_treino.analisar_desempenho(tempo)
diferenca_meta, status, msg = funcoes_treino.consolidar_treino(calorias_totais, meta_semanal)

os.system('cls')

funcoes_treino.separador()
print('PUC Minas - Treino'.center(50))
funcoes_treino.separador()

print(f'Calorias Totais: {calorias_totais}')
print(f'Tempo Total: {tempo_total}')
print(f'Horas: {horas}')
print(f'Minutos: {minutos}')
print(f'Diferença: {diferenca_meta}')
print(f'Status: {status}')
print(f'Situação: {msg}')

funcoes_treino.separador()
