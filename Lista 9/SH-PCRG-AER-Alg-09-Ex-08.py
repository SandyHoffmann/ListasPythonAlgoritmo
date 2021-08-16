import os
import sys
def elimina_simbolos(string):
    simbolos_eliminar = ["?", ",",".","!"]
    for s in simbolos_eliminar:
        string = string.replace(s,"")
    return string

try:
    x = 0
    caminho = os.path.abspath(f'{sys.argv[1]}')
    reverse = []
    maior_comprimento = 0
    lista_palavras = []
    dic_letras = {}

    with open(caminho, "r", encoding="utf8") as file:
        for line in file:
            line = line.rstrip()
            line = elimina_simbolos(line)
            line = line.lower()
            if line in dic_letras.keys():
                dic_letras[line]+=1
            else:
                dic_letras[line] = 1

    def get_key(val):
        keys = []
        for key, value in dic_letras.items():
            if val == value:
                keys.append(key)
        return keys
    max = dic_letras[max(dic_letras, key=dic_letras.get)]
    print(f'Num ocorrencias = {max} - {get_key(max)}')

except FileNotFoundError:
    print("Não foi possivel encontrar o arquivo!")
