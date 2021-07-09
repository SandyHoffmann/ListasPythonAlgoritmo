def calcular_div(numero):
    divisores=[]
    for x in range(1,numero+1):
        if numero%x==0:
            divisores.append(x)
    return divisores