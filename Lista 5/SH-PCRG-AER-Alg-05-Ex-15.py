def hex2int(string):
    total = 0
    tam_string = len(string)
    for x in range(tam_string):
        if string[x] == 'a':
            conta=10*(16**x)
        elif string[x] == 'b':
            conta=11*(16**x)
        elif string[x] == 'c':
            conta=12*(16**x)
        elif string[x] == 'd':
            conta=13*(16**x)
        elif string[x] == 'e':
            conta=14*(16**x)
        elif string[x] == 'f':
            conta=15*(16**x)
        else:
            conta = int(string[x])*(16**x)
        conta = conta*(10**(tam_string-1-x))
        print(conta)
        total+=conta
    return total
def int2hex(inteiro):
    pass

def main():
    string = input('Me diga um numero para converter: ')
    print(hex2int(string))

if __name__ == "__main__":
    main()