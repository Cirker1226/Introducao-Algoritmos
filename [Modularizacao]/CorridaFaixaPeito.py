def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
   
def contar_pares_faixa(inicio,fim):
    contador = 0
    for numero in range (inicio, fim):
        if eh_par(numero):
            contador += 1
    return contador

inicio = int(input('Digite um valor inicial: '))
fim = int(input('Digite o valor final: '))

resultado = contar_pares_faixa(inicio, fim + 1)

print(f'A quantidade de números pares é: {resultado}')