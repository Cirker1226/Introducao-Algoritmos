import os
os.system ('cls')
 
massa = float(input('Digite a Massa inicial do material: '))
 
save_massa = massa
tempo = 0
 
while massa > 0.5:
    massa = massa / 2
    tempo += 50
 
print(f'Massa Inicial: {save_massa}g')
print(f'Massa final: {massa:.2f}g')
print(f'Tempo total: {tempo} segundos')