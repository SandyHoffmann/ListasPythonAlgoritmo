def mapear(x):
    if x.isdigit() == False:
        return x 
        
def is_null(str):
    if str.isdigit() == False:
        return True
    else:
        return False

def cod_run_lenght(string):
    resultado = map(mapear,filter(is_null,string))
    resultado = list(resultado)

    def teste(x,index=[]):

        if len(x) != 0:
            resultado = x[0]
            if index == []:
                index.append(resultado)
                index.append(0)
            if index[-2] == resultado:
                index[-1] = index[-1]+1
            if index[-2] != resultado:
                index.append(resultado)
                index.append(1)
            x.pop(0)
            return teste(x,index)
        else:
            return index
    return teste(resultado)

def main():
    print(f'Decodificada = {cod_run_lenght("AAAAAABBAAACCAABVBB")}')

if __name__ == "__main__":
    main()

