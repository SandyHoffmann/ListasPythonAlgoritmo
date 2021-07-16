from precedenciapy import precedencia
def postfix(lista_token):
    operadores = []
    postfix = []
    for token in lista_token:
        if type(token) == int:
            postfix.append(token)
        if (token == "+" or token == "-" or token == "*" or token == "/" or token == "^"):
            if len(operadores)>0:
                while len(operadores)>=0 and operadores[-1] != "(" and precedencia(token)<precedencia(operadores[-1]):
                    postfix.append(operadores[-1])
                    operadores.pop(-1)
            operadores.append(token)
        if token == "(":
            operadores.append(token)
        if token == ")":
            while (operadores[-1]!="("):
                postfix.append(operadores[-1])
                operadores.pop(-1) 
            operadores.pop(-1)
    while len(operadores)>0:
        postfix.append(operadores[-1])
        operadores.pop(-1) 
    return(postfix)

def toToken(exprecao):
    lista = []
    exprecao.replace(" ", "")
    elemento_ant = ""
    contador = -1
    for elemento in exprecao:
        contador+=1
        if elemento == "(":
            lista.append(elemento)
        elif (elemento == "*" or elemento == "/" or elemento == "^" or elemento == "-" or elemento == "+" or elemento == "(" or elemento == ")") and elemento_ant!="":
            lista.append(int(elemento_ant))
            lista.append(elemento)
            elemento_ant = ""
        else:
            if elemento!="":
                elemento_ant+=elemento
        if contador == len(exprecao)-1 and elemento!=")":
            lista.append(int(elemento_ant))

    return lista

def main():
  token = input("Dê-me um token: ")
  print(postfix(toToken(token)))
  
if __name__ == "__main__":
    main()
        
