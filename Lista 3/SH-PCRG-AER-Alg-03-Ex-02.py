#Pedindo os anos do cachorro
idade = int(input("Quantos anos tem o seu dog? "))
#Se idade for numero negativo n pode ser considerado.
if idade<0:
    print(f'Dados inválidos!')
#Se idade menor ou igual a dois calcularemos conforme foi dito pelo enunciado
elif idade<=2:
    print(f'A idade do cachorro é de {idade*10.5} anos.')
#Se for maior q dois, deixaremos o calculo usando o 10.5 ali e acrescentaremos o resto da idade multiplicando 4.
else:
    print(f'A idade do cachorro é de {2*10.5+idade*4} anos.')