#Pegando as medidas do triângulo
lado_a = int(input("Qual é a medida do lado A? "))
lado_b = int(input("Qual é a medida do lado B? "))
lado_c = int(input("Qual é a medida do lado C? "))

#Checando se ele tem os três lados iguais
if lado_a == lado_b and lado_b == lado_c:
    print("É um triângulo equilátero.")
#Checando se ele tem os três lados diferentes
elif lado_a!=lado_b and lado_b!=lado_c and lado_c!=lado_a:
    print("É um triângulo escaleno.")
#Caso n seja nenhuma das acima, só sobra a opção de ele ter dois lados iguais.
else:
    print("É um triângulo isósceles.")

