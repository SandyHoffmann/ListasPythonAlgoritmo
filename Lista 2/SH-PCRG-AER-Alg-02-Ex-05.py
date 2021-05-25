#Pedindo os centavos.
centavos = int(input("Diga os centavos: "))

#Descobrindo a quantidade de moedas
moeda50 = centavos//50
moeda25 = (centavos - (moeda50*50))//25
moeda10 = (centavos - (moeda50*50) - (moeda25*25))//10
moeda5 = (centavos - (moeda50*50) - (moeda25*25) - (moeda10*10))//5
moeda1 = (centavos - (moeda50*50) - (moeda25*25) - (moeda10*10) - (moeda5*5) )//1

#Printando as moedas
print(f'moedas 50 - {moeda50}')
print(f'moedas 25 - {moeda25}')
print(f'moedas 10 - {moeda10}')
print(f'moedas 5 - {moeda5}')
print(f'moedas 1 - {moeda1}')