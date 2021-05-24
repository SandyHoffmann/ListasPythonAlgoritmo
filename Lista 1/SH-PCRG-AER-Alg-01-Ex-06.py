#Pedindo valores
suco = float(input("Qual o valor do suco? "))
prato_principal = float(input("Qual o valor do prato principal? "))
sobremesa = float(input("Qual o valor da sobremesa? "))

#Somando os valores e acrescentando 10% em cima
conta = (suco+prato_principal+sobremesa)*1.10

#Mostrando na tela com o arredondamento.
print(f'O total da sua conta é de {conta:.2f} R$')
