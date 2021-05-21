#Pedindo a quantidade de vasilhames de cada tipo
vasilhame_menor = float(input("Me diga a quantidade de vasilhames de 1 litro ou menos: "))
vasilhame_maior = float(input("Me diga a quantidade de vasilhames com mais de 1 litro: "))

#Fazendo as contas de acordo com o tipo de vasilhame
conta_vasilhame_menor = vasilhame_menor * 0.10
conta_vasilhame_maior = vasilhame_maior * 0.25

#Somando o valor total
total_conta = conta_vasilhame_maior+conta_vasilhame_menor

#Mostrando o resultado no terminal e arredondando.
print(f'O total de valor a ganhar é de {total_conta:.2f} R$')
