import math
#definindo variaveis bases
perimetro = 0
x1=0
y1=0
#loop infinito
while (True):
    #perguntando valor x
    x = (input("Mê de o valor de x: "))
    #vendo se x é vazio
    if x == "":
        break
    #caso n seja, x vira float e é perguntado y tbm
    x = float(x)
    y = float(input("Mê de o valor de y: "))
    #faz-se o calculo da distancia
    distancia = math.sqrt((x1 - x)**2 + (y1 - y)**2)
    #e se soma no perimetro
    perimetro+=distancia
    #substitui-se x1 e x2 pelos anteriores
    x1=x
    y1=y

#mostrando na tela
print(f'O perimetro total é de {perimetro}')
