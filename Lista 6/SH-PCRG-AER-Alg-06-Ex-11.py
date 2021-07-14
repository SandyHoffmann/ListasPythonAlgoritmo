import random
def mega():
    lista_num = []
    for x in range(0,60):
        bilhete = []
        for y in range(6):
            numero = random.randint(0,100)
            bilhete.append(numero)
        if len(lista_num)>0:
            contador = 0
            for i in lista_num:
                contador = 0
                for x in i:
                    if len(bilhete)>0:
                        if x == bilhete[contador]:
                            bilhete =[]
                        else:
                            contador+=1
        if len(bilhete)>0:
            lista_num.append(bilhete)
    print(lista_num)

def main():
    mega()

    
if __name__ == "__main__":
    main()
