def ver_ord(lista):
    lista_ord = lista.copy()
    lista_ord.sort()
    lista_rev = lista_ord.copy()
    lista_rev.reverse()
    flag = True
    tipo = True
    for e in range(len(lista)):
        if tipo!=False:
            if lista[e] == lista_ord[e]:
                flag = True
                tipo = True
            else:
                tipo = False
    if tipo == False:
        for e in range(len(lista)):
            if lista[e] == lista_rev[e]:
                flag = True
            else:
                flag = False
                return(flag)

    if tipo == True:
        return("Esta ordenada em Crescente")
    else:
        return("Esta ordenada em Decrescente")
def main():
    lista = []
    item = "teste"
    while item != "":
        item = str(input("Digite um num para a lista: "))  
        if item != "":
            lista.append(int(item))
    resultado = ver_ord(lista)
    if(resultado):
        print(resultado)
    else:
        print("Lista não ordenada!")
    
if __name__ == "__main__":
    main()
