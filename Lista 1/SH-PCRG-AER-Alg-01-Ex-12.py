import math

#Pedindo o raio
raio = float(input("Me dê o raio: "))

#Calculando área e volume
area_circulo = math.pi*(raio**2)
volume = (4/3)*math.pi*(raio**3)

#Mostrando no terminal
print(f'A área do circulo é de {area_circulo}\nO volume da esfera é de {volume}')


