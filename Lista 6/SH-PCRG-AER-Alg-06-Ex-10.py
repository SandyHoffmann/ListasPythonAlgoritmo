def formataStr(lista):
    novastr = ""
    for x in range(len(lista)):
        if x==(len(lista)-1):
            novastr +=lista[x]
        elif x == (len(lista)-2):
            novastr += f'{lista[x]} e '
        else:
            novastr += f'{lista[x]}, '
    return novastr

def main():
    lista = []
    item = "teste"
    while item != "":
        item = str(input("Digite um item para a lista: "))  
        if item != "":
            lista.append(item)
    
    resultado = formataStr(lista)
    print(resultado)
    
if __name__ == "__main__":
    main()