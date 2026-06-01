numeros = []

for i in range(7):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

palindromo = True

for i in range(len(numeros) // 2):
    if numeros[i] != numeros[len(numeros) - 1 - i]:
        palindromo = False

if palindromo:
    print("A lista é palíndromo.")
else:
    print("A lista não é palíndromo.")