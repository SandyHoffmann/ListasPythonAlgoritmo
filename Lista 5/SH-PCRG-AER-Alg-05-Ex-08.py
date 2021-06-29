
def arrumar_frase(frase):
    frase = frase.capitalize()
    frase_nova = frase.split(" ")
    frasetam= len(frase_nova)
    for x in range(frasetam):
        frase = frase_nova[x]
        if (frase.count('?') != 0) or (frase.count('!') != 0) or (frase.count('.') != 0) :
            if x<(frasetam-1):
                frase_nova[x+1] = frase_nova[x+1].capitalize()     
    frase_certa = ' '.join(frase_nova)
    return(frase_certa)

def main():
    frase = input("Qual é a frase? ")
    print(f'{arrumar_frase(frase)}')

if __name__ == "__main__":
    main()