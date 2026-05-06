import os
os.system('cls')

total_vendido = 0
quantidade_vendas = 0

qtd_lanche = 0
qtd_bebida = 0
qtd_sobremesa = 0

opcao = -1

while opcao != 0:
    print("\n1 - Registrar venda")
    print("2 - Mostrar total vendido")
    print("3 - Mostrar quantidade de vendas")
    print("4 - Mostrar valor médio das vendas")
    print("5 - Mostrar quantidade vendida por tipo de produto")
    print("0 - Encerrar sistema")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        codigo = int(input("Digite o código do produto (1-Lanche, 2-Bebida, 3-Sobremesa): "))
        valor = float(input("Digite o valor da venda: "))

        if codigo < 1 or codigo > 3:
            print("Erro: código de produto inválido.")
        elif valor <= 0:
            print("Erro: valor de venda inválido.")
        else:
            total_vendido = total_vendido + valor
            quantidade_vendas = quantidade_vendas + 1

            if codigo == 1:
                qtd_lanche = qtd_lanche + 1
            elif codigo == 2:
                qtd_bebida = qtd_bebida + 1
            else:
                qtd_sobremesa = qtd_sobremesa + 1

            print("Venda registrada com sucesso.")

    elif opcao == 2:
        print("Total vendido =", total_vendido)

    elif opcao == 3:
        print("Quantidade de vendas =", quantidade_vendas)

    elif opcao == 4:
        if quantidade_vendas > 0:
            media = total_vendido / quantidade_vendas
        else:
            media = 0

        print("Valor médio das vendas =", media)

    elif opcao == 5:
        print("Quantidade de vendas de lanche =", qtd_lanche)
        print("Quantidade de vendas de bebida =", qtd_bebida)
        print("Quantidade de vendas de sobremesa =", qtd_sobremesa)

    elif opcao == 0:
        print("\nEncerrando sistema...")

    else:
        print("Erro: opção inválida.")

if quantidade_vendas > 0:
    media = total_vendido / quantidade_vendas
else:
    media = 0

print("\nRelatório final")
print("Total vendido =", total_vendido)
print("Quantidade total de vendas =", quantidade_vendas)
print("Valor médio das vendas =", media)
print("Quantidade de vendas de lanche =", qtd_lanche)
print("Quantidade de vendas de bebida =", qtd_bebida)
print("Quantidade de vendas de sobremesa =", qtd_sobremesa)