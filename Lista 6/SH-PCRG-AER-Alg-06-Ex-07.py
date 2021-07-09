import calcular_divisores

def verificar_perfeicao(numero):
    lista = calcular_divisores.calcular_div(numero)
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

