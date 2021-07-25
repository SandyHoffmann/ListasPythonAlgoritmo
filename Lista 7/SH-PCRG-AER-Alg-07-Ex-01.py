def verificar(string):
    lista = []
    lista[:0] = string
    reversa = lista.copy()
    reversa.reverse()
    contador = 0
    for letra in lista:
        for l in reversa:
            if letra == l: 
                contador+=1
                if contador>1:
                    return False
        contador=0
    return True

def main():
    palavra = input("Qual a palavra? ")
    print(verificar(palavra))

if __name__ == "__main__":
    main()
