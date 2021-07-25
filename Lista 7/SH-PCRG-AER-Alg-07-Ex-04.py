def to_morse(frase):
    dic = {"A":".-","B":"-...","C":"-.-.",
            "D":"-..","E":".","F":"..-.",
            "G":"--.","H":"....","I":"..",
            "J":".---","K":"-.-","L":".-..",
            "M":"--","N":"-.","O":"---",
            "P":".--.","Q":"--.-","R":".-.",
            "S":"...","T":"-","U":"..-",
            "V":"...-","W":".--","X":"-..-",
            "Y":"-.--","Z":"--..","0":"-----",
            "1":".----","2":"..---","3":"...--",
            "4":"....-","5":".....","6":"-....",
            "7":"--...","8":"---..","9":"----."}

    frase = frase.upper()
    frase = frase.replace(" ","")
    nova_frase_morse = ""
    for e in frase:
        for i in dic.keys():
            if e == i:
                nova_frase_morse+=dic[i]+" "
    return(nova_frase_morse)

def main():
    print(to_morse("Hello, World!"))
    
if __name__ == "__main__":
    main()
