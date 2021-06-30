def hex2int(string):
    string = string.lower()
    if len(string)>1:
        return("Não foi possivel a conversão!")
    elif string == 'a':
        conta=10
    elif string == 'b':
        conta=11
    elif string == 'c':
        conta=12
    elif string == 'd':
        conta=13
    elif string == 'e':
        conta=14
    elif string == 'f':
        conta=15
    else:
        conta = int(string)
    return conta

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