numeros = []

for i in range(10):
    numeros.append(int(input("Informe um valor númerico: ")))

maior = numeros[0]
segundo_maior = None

for numero in numeros[1:]:
    if numero > maior:
        segundo_maior = maior
        maior = numero
    elif numero != maior:
        if numero > segundo_maior:
            segundo_maior = numero

print("Maior valor:", maior)
print("Segundo maior valor:", segundo_maior)