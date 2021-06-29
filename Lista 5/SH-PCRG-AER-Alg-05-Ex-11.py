import random
def forma_senha():
    comprimento = random.randint(7,10)
    frase = ''
    for x in range(comprimento):
        letra = random.randint(33,126)
        frase+=chr(letra)
    return frase

def main():
    print(forma_senha())

if __name__ == "__main__":
    main()