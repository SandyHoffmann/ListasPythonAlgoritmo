def fatorial(numero):
    if numero == 1:
        return numero
    else:
        novo_numero = numero * fatorial(numero-1)
        return novo_numero

def main():
    num = int(input("Fatorial de que numero? "))
    print(fatorial(num))

if __name__ == "__main__":
    main()

