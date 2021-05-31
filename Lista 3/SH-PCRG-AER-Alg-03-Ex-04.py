#Pedindo quantos lados tem o poligono.
lado_poligono = int(input("Quantos lados tem o poligono? "))
#Checando as formas de acordo com os lados, primeiro já checando se o usuario informou numeros no parametro certo.
if lado_poligono<3 or lado_poligono>10:
    print("Não é possivel encontrar formas com esses lados.")
elif lado_poligono ==3:
    print()
#Terminar ATVDD
#Se n for encontrado retorna uma mensagem de erro.
else:
    print("Não foi encontrado mês com esse nome.")