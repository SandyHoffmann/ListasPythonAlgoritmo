fator = 2
inteiro = int(input("Me diga um numero: "))
divisao = inteiro
if divisao<2:
    print("erro")
else:
    while fator<=divisao:
        if divisao%fator==0:
            print(fator)
            divisao = divisao//fator
        else:
            fator+=1
        