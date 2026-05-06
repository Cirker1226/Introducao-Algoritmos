def separador():
    print('-'*50)

def calcular_valor_base(tipo_ingresso, valor_padrao=120):
    if tipo_ingresso == "regular":
        valor_ingresso = valor_padrao * (100/100)
    elif tipo_ingresso == "vip":
        valor_ingresso = valor_padrao * (150/100)
    elif tipo_ingresso == "estudante":
        valor_ingresso = valor_padrao * (60/100)
    else:
        valor_ingresso = 0

    return valor_ingresso

def calcular_extras(valor_base, oficinas=0, material_extra=False):
    total_oficinas = oficinas * 30
    valor_material = material_extra * 20
    valor_parcial = valor_base + total_oficinas + valor_material

    return total_oficinas, valor_material, valor_parcial

def aplicar_desconto(valor_parcial, cupom=0, taxa_admin=5):
    valor_desconto = valor_parcial * (cupom / 100)
    valor_com_desconto = valor_parcial - valor_desconto
    valor_taxa = valor_com_desconto * (taxa_admin / 100)
    valor_final = valor_com_desconto + valor_taxa

    return valor_desconto, valor_taxa, valor_final

def classificar_participacao(oficinas, material_extra, total_final):
    if oficinas >= 2 and material_extra > 0:
        msg = "Inscrição completa"
    elif oficinas >= 1:
        msg = "Inscrição intermediária"
    else:
        msg = "Inscrição básica"

    return msg

def gerar_relatorio_participante(nome, tipo_ingresso, valor_padrao, oficinas, material_extra, cupom=0):

    valor_base = calcular_valor_base(tipo_ingresso, valor_padrao)
    valor_oficinas, valor_material, valor_parcial = calcular_extras(valor_base, oficinas, material_extra)
    valor_desconto, valor_taxa_admin, valor_final = aplicar_desconto(valor_parcial, cupom)
    classificacao = classificar_participacao(oficinas, material_extra, valor_final)

    return valor_base, valor_oficinas, valor_material, valor_desconto, valor_taxa_admin, valor_final, classificacao