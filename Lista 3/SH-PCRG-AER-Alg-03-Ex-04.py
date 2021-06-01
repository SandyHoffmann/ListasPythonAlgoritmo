#Pedindo quantos lados tem o poligono.
lado_poligono = int(input("Quantos lados tem o poligono? "))
#Checando as formas de acordo com os lados, primeiro já checando se o usuario informou numeros no parametro certo.
if lado_poligono<3 or lado_poligono>10:
    print("Não foi possivel encontrar formas com esses lados.")
elif lado_poligono ==3:
    print("É um Triangulo")
elif lado_poligono ==4:
    print("É um Quadrado")
elif lado_poligono ==5:
    print("É um Pentagono")
elif lado_poligono ==6:
    print("É um Hexágono")
elif lado_poligono ==7:
    print("É um Heptágono")
elif lado_poligono ==8:
    print("É um Octágono")
elif lado_poligono ==9:
    print("É um Eneágono")
else:
    print("É um Decágono")