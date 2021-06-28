#Pedindo a frase
frase = input("Me dê uma frase: ")
#Variavel para vê-la ao contrario
frasepalindromo = ""
frasenova = ""
frase = frase.lower()
frase = frase.replace(" ", "")

#Conseguindo-a ao contrario
for elemento in frase:
    if((ord(elemento)>64 and ord(elemento)<91) or (ord(elemento)>96 and ord(elemento)<123)):
        frasepalindromo = elemento + frasepalindromo
        frasenova += elemento
#Checando se é um parindromo ou não.
if frasepalindromo == frasenova:
    print(f'A frase {frasenova} é um Palíndromo.')
else:
    print(f'A frase {frasenova} NÃO é um Palíndromo.')

