def ordem(lista1,lista2):
    conj_asc = []
    for e in lista1:
        for i in lista2:
            if e == i:
                if e not in conj_asc:
                    conj_asc.append(e)
    nova_lista = []
    for e in lista1:
        if e not in conj_asc:
            nova_lista.append(e)
    for e in lista2:
        if e not in conj_asc:
            nova_lista.append(e)
    return nova_lista

def main():
    lista1 = []
    lista2 = []
    quant_elem = int(input("Qual o numero de elementos que você gostaria de pôr em cada lista: "))
    for x in range(quant_elem):
        numero = int(input("Qual o novo numero para a lista 1? "))
        lista1.append(numero)
    for y in range(quant_elem):
        numero = int(input("Qual o novo numero para a lista 2? "))
        lista2.append(numero)
    print(ordem(lista1,lista2))

if __name__ == "__main__":
    main()

