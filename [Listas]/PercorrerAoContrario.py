lista = []

for i in range(8):
    
    palavras = input('Informe uma palavra: ')
    lista.append(palavras)

for palavra in range(len(lista) - 1, -1, -1):

    print(lista[palavra])