import os
import sys

try:
    argumentos = []
    for i, arg in enumerate(sys.argv):
        argumentos.append(arg)
    argumentos.pop(0)
    ultimoarq = argumentos.pop(-1)
    print(ultimoarq)
    print(argumentos)
    contador = 0
    caminho = os.path.abspath(ultimoarq)
    with open(caminho, 'w') as outfile:
        for a in argumentos:
            caminho = os.path.abspath(a)
            with open(caminho, "r", encoding="utf8") as file:
                for line in file:
                    if line[0] == "#":
                        pass
                    else:
                        outfile.write(line)

except FileNotFoundError:
    print("Não foi possivel encontrar o arquivo!")