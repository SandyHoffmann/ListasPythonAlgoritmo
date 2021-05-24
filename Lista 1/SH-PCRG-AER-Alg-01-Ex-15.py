import math

#Pegando as informações do poligono
l = float(input("Me diga o comprimento: "))
n = int(input("Me diga o numero de lados: "))

#Fazendo a conta
area = (n*(l**2))/(4*math.tan(math.pi/n))

#Mostrando no terminal
print(f'A área do poligono é de {area}')
