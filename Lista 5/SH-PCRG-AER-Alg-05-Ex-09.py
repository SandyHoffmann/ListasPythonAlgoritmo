
def isInteger(string):
    string = string.strip()
    listapossibilidade = ['0','1','2','3','4','5','6','7','8','9']
    count = 0
    tamanhostr = len(string)
    if string[0] == '+':
        tamanhostr-=1
    elif string[0] == '-':
        tamanhostr-=1

    if tamanhostr:
        for letra in string:
            for possibilidade in listapossibilidade:
                if letra == possibilidade:
                    count+=1
                    
    if tamanhostr==count:
        return True
    else:
        return False

def main():
    string = input("Qual é a palavra? ")
    ehstr = isInteger(string)
    if ehstr == True:
        print(f'{isInteger(string)} : {string} é um número! ')
    else:
        print(f'{isInteger(string)} : {string} NÃO é um número! ')


if __name__ == "__main__":
    main()