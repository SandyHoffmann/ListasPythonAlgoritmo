#pedindo variaveis
msg = input("Me de sua frase: ")
distancia = int(input("Me dê a distancia de deslocamento: "))
msgletras = list(msg)
novafrase = ""
#percorrendo lista de letras
for letra in msgletras:
    ordem = ord(letra)
    novaletra = chr(ordem+distancia)
    novafrase+=novaletra

#mostrando mensagem final
print(novafrase)