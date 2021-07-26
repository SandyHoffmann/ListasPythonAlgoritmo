def anagrama(frase1,frase2):
    frase1 = frase1.lower()
    frase2 = frase2.lower()
    for x in [" ",".","?","!",":",";",","]:
        frase1 = frase1.replace(x,"")
        frase2 = frase2.replace(x,"")
    frase1dic = transf_dic(frase1)
    frase2dic = transf_dic(frase2)
    print(frase1dic)
    print(frase2dic)
    flag = False
    for key in frase1dic.keys():
        for twokey in frase2dic.keys():
            if twokey == key:
                flag = True
                if frase1dic[key] != frase2dic[twokey]:
                    return False
        if flag == False:
            return False
    return True

def transf_dic(frase):
    dicfrase = {}
    lista = []
    lista[:0] = frase
    for e in frase:
        if dicfrase.get(e):
            dicfrase[e]+=1
        else:
            dicfrase[e]=1
    return(dicfrase)



def main():
    frase1 = input("Me dê a frase 1: ")
    frase2 = input("Me dê a frase 2: ")

    print(anagrama(frase1,frase2))
    
if __name__ == "__main__":
    main()

