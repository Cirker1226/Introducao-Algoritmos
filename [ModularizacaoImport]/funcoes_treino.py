def separador():
    print('-'*50)

def calcular_calorias(calorias_base, bonus=0):
    calorias_totais = calorias_base + bonus

    return calorias_totais

def calcular_tempo_treino(tempo_principal, aquecimento=10):
    tempo_total = tempo_principal + aquecimento

    return tempo_total

def analisar_desempenho(total_minutos):
    horas = total_minutos // 60
    minutos = total_minutos % 60

    return horas, minutos

def consolidar_treino(calorias, meta=300):
    diferenca_meta = calorias - meta
    
    if calorias >= meta:
        msg = "Meta atingida!"
        status = True
        
    elif calorias < meta:
        msg = "Meta não atingida!"
        status = False
    else:
        msg = "Erro!"

    return diferenca_meta, status, msg