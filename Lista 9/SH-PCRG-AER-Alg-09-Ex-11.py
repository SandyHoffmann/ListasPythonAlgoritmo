import os
import sys
def elimina_simbolos(string):
    simbolos_eliminar = ["?",",",".","!"]
    string2 = string
    for s in simbolos_eliminar:
        string = string.replace(s,"")
    if string2 != string:
        return False
    return True

try:
    x = 0
    caminho = os.path.abspath(f'{sys.argv[1]}')
    caminho2 = os.path.abspath(f'{sys.argv[2]}')
    lista_palavras = []
    dic_letras = {}

    with open(caminho, "r", encoding="utf8") as file:
        for line in file:
            line = line.rstrip()
            line = line.lower()
            if line in dic_letras.keys():
                dic_letras[line]+=1
            else:
                dic_letras[line] = 1
    with open(caminho2, "r", encoding="utf8") as file2:
        for line2 in file2:
            line2 = line2.rstrip()
            line2 = line2.split(" ")
            for l in line2:
                l = l.lower()
                if elimina_simbolos(l) == True:
                    if l in dic_letras.keys():
                        pass
                    else:
                        lista_palavras.append(l)

    print(lista_palavras)

except FileNotFoundError:
    print("Não foi possivel encontrar o arquivo!")