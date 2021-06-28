from typing import FrozenSet


#Pedindo a frase
frase = input("Me dê uma frase: ")
#Variavel para vê-la ao contrario
frasepalindromo = ""

#Conseguindo-a ao contrario
for elemento in frase:
    frasepalindromo = elemento + frasepalindromo

#Checando se é um parindromo ou não.
if frasepalindromo == frase:
    print(f'A palavra {frase} é um Palíndromo.')
else:
    print(f'A palavra {frase} NÃO é um Palíndromo.')

