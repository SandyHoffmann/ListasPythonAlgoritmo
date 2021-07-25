def anagrama(palavra1,palavra2):
    palavra1dic = transf_dic(palavra1)
    palavra2dic = transf_dic(palavra2)
    print(palavra1dic)
    print(palavra2dic)
    flag = False
    for key in palavra1dic.keys():
        for twokey in palavra2dic.keys():
            if twokey == key:
                flag = True
                if palavra1dic[key] != palavra2dic[twokey]:
                    return False
        if flag == False:
            return False
    return True

def transf_dic(palavra):
    dicpalavra = {}
    lista = []
    lista[:0] = palavra
    for e in palavra:
        if dicpalavra.get(e):
            dicpalavra[e]+=1
        else:
            dicpalavra[e]=1
    return(dicpalavra)

def main():
    palavra1 = input("Me dê a palavra 1: ")
    palavra2 = input("Me dê a palavra 2: ")

    print(anagrama(palavra1,palavra2))
    
if __name__ == "__main__":
    main()

