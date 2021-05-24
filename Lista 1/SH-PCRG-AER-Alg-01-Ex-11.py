import math

#Pedindo dados primeiro ponto
latitude1 = float(input("Me dê a latitude do ponto 1: "))
longitude1 = float(input("Me dê a longitude do ponto 1: "))

#Pedindo dados segundo ponto
latitude2 = float(input("Me dê a latitude do ponto 2: "))
longitude2 = float(input("Me dê a longitude do ponto 2: "))

#Implementando a conta
distancia = 6371.01 * math.acos(math.sin(math.radians(latitude1)) * math.sin(math.radians(latitude2)) + math.cos(math.radians(latitude1)) * math.cos(math.radians(latitude2)) * math.cos(math.radians(longitude1) - math.radians(longitude2)))

#Mostrando no terminal
print(f'A distância entre esses pontos é de {distancia}')
