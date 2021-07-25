def buscaReversa(dic,valor_pesq):
    lista_chaves = []
    for e in dic.keys():
        if dic[e] == valor_pesq:
            lista_chaves.append(e)
    return(lista_chaves)

def main():
    dic = {"key1":1,"key2":2,"key3":2,"key4":1}
    print(buscaReversa(dic,2))
if __name__ == "__main__":
    main()

