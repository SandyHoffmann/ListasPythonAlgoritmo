#Perguntando o nome da nota, e separando a letra do numero.
nome_nota = input("Me dê o nome da nota: ").lower()
letra = nome_nota[0]
numero = int(nome_nota[1])

"""Checando as condições e fazendo a conta, ja que separei a letra do numero, ficando assim muito mais
fácil de calcular as frequências sonoras."""

if letra == "a":
    frequencia = 440.00/2**(4-numero)
    print(f'A frequencia da nota {nome_nota} é de: {frequencia}Hz')

elif letra == "b":
    frequencia = 493.88/2**(4-numero)
    print(f'A frequencia da nota {nome_nota} é de: {frequencia}Hz')

elif letra == "c":
    frequencia = 261.63/2**(4-numero)
    print(f'A frequencia da nota {nome_nota} é de: {frequencia}Hz')

elif letra == "d":
    frequencia = 293.66/2**(4-numero)
    print(f'A frequencia da nota {nome_nota} é de: {frequencia}Hz')

elif letra == "e":
    frequencia = 329.63/2**(4-numero)
    print(f'A frequencia da nota {nome_nota} é de: {frequencia}Hz')

elif letra == "g":
    frequencia = 392.00/2**(4-numero)
    print(f'A frequencia da nota {nome_nota} é de: {frequencia}Hz')
else:
    print("Não foi possivel encontrar a nota musical escolhida.")