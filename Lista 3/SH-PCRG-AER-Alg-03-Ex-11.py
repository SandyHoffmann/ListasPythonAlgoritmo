#importando biblioteca
import math

#Pedindo valores a, b e c
a = int(input("Me de o valor de A: "))
b = int(input("Me de o valor de B: "))
c = int(input("Me de o valor de C: "))

#Fazendo determinante
delta = b**2 - 4*a*c

#Se for negativo n possui raizes
if delta < 0:
    print("A equação não possui raizes reais.")

#Se for 0 apenas possui uma raiz
elif delta == 0:
    bhaskara = ((b)*-1 + math.sqrt(delta))/(2*a)
    print(f'A equação possui apenas uma raiz real: {bhaskara}.')

#caso n seja uma das cimas, ele possui duas raizes.
else:
    bhaskarapositivo = ((b)*-1 + math.sqrt(delta))/(2*a)
    bhaskaranegativo = ((b)*-1 - math.sqrt(delta))/(2*a)
    print(f'A equação possui duas raizes: {bhaskarapositivo} e {bhaskaranegativo}')


