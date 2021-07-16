def calcular_div(numero):
    divisores=[]
    for x in range(1,numero+1):
        if numero%x==0:
            divisores.append(x)
    return divisores

def verificar_perfeicao(numero):
    lista = calcular_div(numero)
    soma = 0
    for x in range(len(lista)-1):
        soma+=lista[x]
    if soma == numero:
        return True
    return False

def main():
    for x in range(10001):
        if (verificar_perfeicao(x)):
            print(x)

if __name__ == "__main__":
    main()

