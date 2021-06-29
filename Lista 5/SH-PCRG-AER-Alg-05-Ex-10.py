
def isPrimo(primo):
    for x in range(2,primo):
        if primo%x== 0:
            return False
    return True

def main():
    numero = int(input("Qual é o número? "))
    ehpri = isPrimo(numero)
    if numero<0:
        print("Digite valor válido!")
    elif ehpri == True:
        print(f'{isPrimo(numero)} : {numero} é um primo! ')
    else:
        print(f'{isPrimo(numero)} : {numero} NÃO é um primo! ')

if __name__ == "__main__":
    main()