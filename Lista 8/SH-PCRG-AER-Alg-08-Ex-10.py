def mapear(x):
    if type(x) == int:
        return x

def run_lenght(lista):
    resultado = map(mapear,lista)
    lista_result = list(resultado)
    lista_result = set(lista_result)
    lista_result.remove(None)
    lista_result = list(lista_result)
    if lista_result.count(1)==1:
        lista_result.remove(1)
        lista.remove(1)
        if lista_result != []:
            a = lista.pop(0)
            b = lista.pop(0)
            lista.append(a)
            lista.append(b)
            return run_lenght(lista)
        else:
            lista.reverse()
            return lista
    else:
        if lista_result[-1]>0:
            lista.insert(-2,lista[-2])
            lista[-1] = lista[-1]-1

            return run_lenght(lista)



def main():
    print(f'Original = ["A",10,"B",5,"C",1]')
    print(f'Decodificada = {run_lenght(["A",10,"B",5,"C",1])}')

if __name__ == "__main__":
    main()

