import os
import sys

try:
    x = 0
    caminho = os.path.abspath(f'{sys.argv[1]}')
    reverse = []
    maior_comprimento = 0
    lista_palavras = []
    dic_letras = {'a':0,'b':0,'c':0,'d':0,
                    'e':0,'f':0,'g':0,'h':0,
                    'i':0,'j':0,'k':0,'l':0,
                    'm':0,'n':0,'o':0,'p':0,
                    'q':0,'r':0,'s':0,'t':0,
                    'u':0,'v':0,'w':0,'x':0,
                    'y':0,'z':0}

    with open(caminho, "r", encoding="utf8") as file:
        for line in file:
            line = line.strip()
            nao_repetir = []
            for i in line:
                i = i.lower()
                if i not in nao_repetir:
                    if i in dic_letras.keys():
                        dic_letras[i]+=1
                    nao_repetir.append(i)

    def get_key(val):
        keys = []
        for key, value in dic_letras.items():
            if val == value:
                keys.append(key)
        return keys
    min = dic_letras[min(dic_letras, key=dic_letras.get)]
    print(f'Num ocorrencias = {min} - {get_key(min)}')

    print(dic_letras) 

except FileNotFoundError:
    print("Não foi possivel encontrar o arquivo!")