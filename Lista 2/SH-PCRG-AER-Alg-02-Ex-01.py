#Pegando dados de dias, horas, minutos e segundos.

dias = int(input("Quantidade de dias: "))
horas = int(input("Quantidade de horas: "))
minutos = int(input("Quantidade de minutos: "))
segundos = int(input("Quantidade de segundos: "))

#Somando o total do tempo, convertendo as variaveis anteriores para segundos
total_tempo_segundo = (dias*86400) + (horas*3600) + (minutos*60) + segundos

#Mostrando no console
print(f'O total do tempo em segundos é de {total_tempo_segundo} segundos')