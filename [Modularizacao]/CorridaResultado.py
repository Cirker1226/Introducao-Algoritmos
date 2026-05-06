def gerar_resumo_tempo(total_segundos):
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60
    return horas, minutos, segundos

nome = input('Digite o nome do Participante: ')
total_segundos = int(input("Digite o tempo total em segundos: "))

horas, minutos, segundos = gerar_resumo_tempo(total_segundos)

print(f'Participante: {nome} | Tempo: {horas} Horas(s) | {minutos} Minuto(s) | {segundos} Segundo(s)')