#Recebendo o volume do usuário
volume = int(input("Qual o volume em decibéis: "))

#Fazendo as comparações.
if volume>130 or volume<40:
    print(f'O volume {volume} está fora da faixa de sons que estamos vendo.')
elif volume == 130:
    print("É equivalente a uma Britadeira")
elif volume >106:
    print(f'O nível do volume {volume} esta entre a Britadeira e o Cortador de grama.')
elif volume == 106:
    print("É equivalente a um Cortador de grama")
elif volume > 70:
    print(f'O nível do volume {volume} esta entre o Cortador de grama e o Despertador.')
elif volume == 70:
    print("É equivalente a um Despertador")
elif volume > 40:
    print(f'O nível do volume {volume} esta entre o Despertador e a Sala Silenciosa.')
else:
    print("É equivalente a uma Sala Silenciosa.")