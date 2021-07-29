def palindromo(palavra):

    palavra = palavra.replace(' ','')

    if palavra == "":
        return (True)

    elif palavra[0] == palavra[-1]:
        palavra = palavra[1 : -1]
        return(palindromo(palavra))
    else:
        return False

def main():
    palavra = (input("Me diga uma palavra para transformar: "))
    print(palindromo(palavra))


if __name__ == "__main__":
    main()
