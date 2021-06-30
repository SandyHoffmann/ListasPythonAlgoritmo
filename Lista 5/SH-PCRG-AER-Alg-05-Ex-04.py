def calcular_mediana(n1,n2,n3):
    lista_num = [n1,n2,n3]
    lista_num = sorted(lista_num)
    return lista_num[1]


def main():
    n1 = float(input("Digite n1: "))
    n2 = float(input("Digite n2: "))
    n3 = float(input("Digite n3: "))
    print(calcular_mediana(n1,n2,n3))
    
if __name__ == "__main__":
    main()