import math

#Pegando os lados de um triangulo
l1 = float(input("Me de o lado 1 do triangulo: "))
l2 = float(input("Me de o lado 2 do triangulo: "))
l3 = float(input("Me de o lado 3 do triangulo: "))

#Tirando o lado principal
l = (l1+l2+l3)/2

#Fazendo a conta final
conta = math.sqrt(l*(l-l1)*(l-l2)*(l-l3))

#Exibindo resultado
print(f'A área do triangulo é de {conta}')
