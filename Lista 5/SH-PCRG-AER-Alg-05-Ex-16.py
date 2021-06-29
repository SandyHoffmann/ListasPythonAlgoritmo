def x_to(base,inteiro):
    soma_total = 0
    valor = 0
    resto = 1
    listaval = []
    if base!=16:
        valor = inteiro
        while resto>0:
            valor = valor//base
            resto = valor%base
            if resto:
                listaval.append(resto)
            else:
                listaval.append(valor)
    return listaval


def int2hex(inteiro):
    if inteiro>15 or inteiro<0:
        return("Não foi possivel a conversão!")
    elif inteiro==15:
        hex = 'f'
    elif inteiro==14:
        hex = 'e'
    elif inteiro==13:
        hex = 'd'
    elif inteiro==12:
        hex = 'c'
    elif inteiro==11:
        hex = 'b'
    elif inteiro==10:
        hex = 'a'
    else:
        hex = str(inteiro)
    return hex

def main():
    inteiro = input('Me diga um numero para converter: ')
    base = int(input('Me diga qual a base: '))
    print(x_to(base,inteiro))

if __name__ == "__main__":
    main()