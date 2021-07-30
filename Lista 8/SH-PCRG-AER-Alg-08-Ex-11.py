def mapear(x):
    if x.isdigit() == False:
        return x 

def is_null(str):
    if str.isdigit() == False:
        return True
    else:
        return False

def cod_run_lenght(string):
    if type(string) == str:
        resultado = map(mapear,filter(is_null,string))
        resultado = list(resultado)
        return cod_run_lenght([resultado,[]])

    elif len(string[0]) != 0:
        x = string[0]
        index = string[1]
        letra = x[0]
        if index == []:
            index.append(letra)
            index.append(0)
        if index[-2] == letra:
            index[-1] = index[-1]+1
        if index[-2] != letra:
            index.append(letra)
            index.append(1)
        x.pop(0)
        return cod_run_lenght([x,index])
    else:
        return string[1]

print(f'Decodificada = {cod_run_lenght("AAAAAABBAAACCAABVBB")}')

