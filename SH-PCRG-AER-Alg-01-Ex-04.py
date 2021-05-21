#Pedindo largura e altura para o usuário
largura = float(input("Me diga a largura em metros: "))
altura = float(input("Me diga a altura em metros: "))

#Armazenando o resultado da conta em uma variável
area = largura*altura

#Convertendo para hectares
hectares = area/10000

#Mostrando o resultado no terminal.
print("A área da sala em hectares é "+str(hectares))