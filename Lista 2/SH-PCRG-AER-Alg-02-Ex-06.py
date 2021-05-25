#
#Pedindo numero
numero = int(input("Diga um numero de 4 digitos: "))

#Fazendo as operações
quarta_casa = numero//1000
terceira_casa = (numero - (quarta_casa*1000))//100
segunda_casa = (numero - (quarta_casa*1000) - (terceira_casa*100))//10
primeira_casa = (numero - (quarta_casa*1000) - (terceira_casa*100) - (segunda_casa*10))//1

#Somando o total
soma = quarta_casa + terceira_casa + segunda_casa + primeira_casa

#Printando o resultado da soma
print(f'A soma dos digitos é {soma}')
