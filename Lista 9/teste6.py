import os
import sys

try:
    x = 0
    caminho = os.path.abspath(f'{sys.argv[1]}')
    reverse = []
    maior_comprimento = 0
    lista_palavras = []
    with open(caminho, "r", encoding="utf8") as file:
        for line in file:
            line = line.strip()
            if len(line)>maior_comprimento:
                maior_comprimento = len(line)
                lista_palavras = []
            if len(line) == maior_comprimento:
                lista_palavras.append(line)


    print(f'Letras: {maior_comprimento} - {lista_palavras}') 

except FileNotFoundError:
    print("Não foi possivel encontrar o arquivo!")
