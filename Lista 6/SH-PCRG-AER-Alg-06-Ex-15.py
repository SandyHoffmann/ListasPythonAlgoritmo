def token(exprecao):
    lista = []
    exprecao.replace(" ", "")
    elemento_ant = ""
    contador = -1
    for elemento in exprecao:
        contador+=1
        if (elemento == "+" or elemento == "-") and elemento_ant != "":
            lista.append(elemento_ant)
            elemento_ant = elemento
        elif (elemento == "*" or elemento == "/" or elemento == "^"):
            lista.append(elemento_ant)
            lista.append(elemento)
            elemento_ant = ""

        else:
            if (elemento_ant == "+" or elemento_ant == "-") and (elemento == "(" ):
                lista.append(elemento_ant)
                lista.append(elemento)
                elemento_ant = ""
            elif elemento == "(":
                lista.append(elemento)
                elemento_ant = ""
                
            elif (elemento != ")"):
                elemento_ant+=elemento
                print(elemento)
            else:
                lista.append(elemento_ant)
                lista.append(elemento)
        if contador == len(exprecao)-1 and elemento!=")":
            lista.append(elemento_ant)
    return lista
def main():
    exp = input("Me de uma expressão: ")
    print(token(exp))

    
if __name__ == "__main__":
    main()
