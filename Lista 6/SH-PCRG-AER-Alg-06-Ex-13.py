def countRange(lista,val_min,val_max):
    el_maior = []
    el_menor = []
    for e in lista:
        if e>=val_max:
            el_maior.append(e)
        elif e<val_min:
            el_menor.append(e)
    total = len(el_maior)+len(el_menor)
    return(total)

def main():
    lista = []
    item = "teste"
    while item != "":
        item = str(input("Digite um num para a lista: "))  
        if item != "":
            lista.append(int(item))
    val_max = int(input("Digite um valor máximo para a lista: "))  
    val_min = int(input("Digite um valor minimo para a lista: "))  
    resultado = countRange(lista,val_min,val_max)
    print(f'{resultado} valores se encaixam no padrão!')
    
if __name__ == "__main__":
    main()
