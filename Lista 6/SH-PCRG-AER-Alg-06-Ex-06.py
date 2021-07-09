
def calcular_div(numero):
    divisores=[]
    for x in range(1,numero+1):
        if numero%x==0:
            divisores.append(x)
    return divisores

def main():
    numero = int(input("Me de um numero: "))
    print(f'Os divisores de {numero} são: {calcular_div(numero)}')

if __name__ == "__main__":
    main()