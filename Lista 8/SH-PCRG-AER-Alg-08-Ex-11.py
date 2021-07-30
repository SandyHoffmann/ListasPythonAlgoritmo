def mapear(x):
    if x.isdigit() == False:
        return x 
        
def is_null(str):
    if str.isdigit() == False:
        return True
    else:
        return False


def checar_qt_letras(lista):
    def teste(x):
        return lista.count(x)
    return teste

def somar(x):
    if len(x) == 1:
        return x[0]
    else:
        return x[0] + somar(x[1:])

def cod_run_lenght(string):
    resultado = map(mapear,filter(is_null,string))
    resultado = list(resultado)
    print(resultado)
    resultado_fil = list(resultado).copy()
    lista_par = [list(set(resultado_fil)), resultado]
    qt_letra = map(checar_qt_letras(resultado),list(set(resultado_fil)))
    qt_letra = list(qt_letra)
    qt_letra.append(None)
    qt_letra.remove(None)
    lista_result = list(resultado)
    opcoes = list(set(resultado_fil))
    soma = somar(qt_letra)
    ocorrencia = string.rfind(str(resultado[soma-1]))
    print(qt_letra)

    if qt_letra != []:
        lista = list(string)
        if string[-1].isdigit() == False:
            lista.append('1')
            print(''.join(lista))
            return cod_run_lenght(''.join(lista))
        if qt_letra[0]>1:
            lista.pop(ocorrencia-1)
            lista[ocorrencia] = str(int(lista[ocorrencia])+1)
            print(''.join(lista))
            return cod_run_lenght(''.join(lista))
        else:
            qt_letra.pop(-1)
            return ''.join(lista)
    # if qt_letra != []:
    #     print("b")
    #     lista = list(string)
    #     if qt_letra[-1]==1:
    #         qt_letra.pop()
    #         opcoes.pop()
    #         if qt_letra == []:
    #             return lista
    #         ocorrencia = string.rfind(opcoes[-1])
    #         print(ocorrencia)
    #         lista.insert(ocorrencia,'1')
    #         lista.pop(ocorrencia-1)
    #         print(''.join(lista))
    #         print("c'")
    #         return lista

    #     else:
    #         print(ocorrencia)
    #         print(len(lista))
    #         lista[ocorrencia+1] = str (int(lista[ocorrencia+1]) + 1)
    #         lista.pop(ocorrencia-1)
    #         print(''.join(lista))
    #         return cod_run_lenght(''.join(lista))
    # else:
    #     lista = list(string)
    #     # lista[ocorrencia+1] = str (int(lista[ocorrencia+1]) + 1)
    #     print(''.join(lista))
    #     return ''.join(lista)

def main():
    print(f'Decodificada = {cod_run_lenght("AAAAAABB")}')

if __name__ == "__main__":
    main()

