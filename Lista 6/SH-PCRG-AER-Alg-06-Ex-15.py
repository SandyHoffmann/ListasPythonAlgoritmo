def token(exprecao):
    lista = []
    exprecao.replace(" ", "")
    elemento_ant = ""
    numero = ""
    contador = -1
    for elemento in exprecao:
        contador+=1
        if (elemento == "+" or elemento == "-") and elemento_ant != "":
            lista.append(elemento_ant)
            elemento_ant = elemento
        else:
            if elemento_ant == "+(" or elemento_ant == "-(":
                lista.append(elemento_ant)
                elemento_ant = elemento
            else:
                elemento_ant+=elemento
                print(elemento)
        if (len(exprecao)-1 == contador):
            lista.append(elemento_ant)
        
    return lista
print(token("+(40+5-40)"))