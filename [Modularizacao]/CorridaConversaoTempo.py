def converter_tempo(total_segundos):
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60
    return horas, minutos, segundos
 
total_segundos = int(input("Digite o tempo total em segundos: "))
 
horas, minutos, segundos = converter_tempo(total_segundos)
 
print(f"\nTempo de prova:")
print(f"  Horas:   {horas}h")
print(f"  Minutos: {minutos}min")
print(f"  Segundos: {segundos}s")