import re

def arrumar_frase(frase):
    frase_nova = re.split("[,.?]",frase)
    frasetam= len(frase_nova)
    print(frase_nova)
     
    frase_certa = ' '.join(frase_nova)
    return(frase_certa)

def main():
    frase = input("Qual é a frase? ")
    print(f'{arrumar_frase(frase)}')

if __name__ == "__main__":
    main()