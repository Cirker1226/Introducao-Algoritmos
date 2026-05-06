import os
os.system ('cls')              

tabuada = 1
 
while tabuada <= 9:
    print(f'Tabuada do {tabuada}:')

    contador = 1
    while contador <= 10:
        multiplicacao = tabuada * contador
        print(f'{tabuada} x {contador} = {multiplicacao}')
        
        contador += 1
 
    print()   
    tabuada += 1