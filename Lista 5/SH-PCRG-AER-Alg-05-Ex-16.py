import hextoint

def x_to(base,inteiro):
    soma_total = 0
    valor = 0
    resto = 1
    listaval = []
    valor = inteiro
    while valor>=1:
        resto = valor%base
        if resto == valor:
            listaval.append(valor)
        else:
            listaval.append(resto)
        valor = valor//base
    if base!=16:
        for x in range(len(listaval)):
            soma_total += listaval[x]*(10**x)
    else:
        soma_total = ''
        for x in range(len(listaval)):
            soma_total+= hextoint.int2hex(listaval[len(listaval)-1-x])

    return(soma_total)


def to_dec(base,inteiro):
    if base!=16:
        inteiro = str(inteiro)
        total = 0
        for x in range(len(inteiro)):
            total+=(int(inteiro[x])*(base**(len(inteiro)-1-x)))
        return(total)
    else:
        total = 0
        cont = 0
        for letra in inteiro:
            total = total + ((hextoint.hex2int(letra)*(16**(len(inteiro)-1-cont))))
            cont+=1
        print(total)
        return(total)

def main():
    inteiro = input('Me diga um numero para converter: ')
    base = int(input('Me diga qual a base que ele esta: '))
    base_nova = int(input('Me diga qual a base qual que vc quer converter: '))
    print(x_to(base_nova,to_dec(base,inteiro)))

if __name__ == "__main__":
    main()
