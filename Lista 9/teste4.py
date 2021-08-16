import os
import sys

try:
    argumentos = []
    for i, arg in enumerate(sys.argv):
        argumentos.append(arg)
    argumentos.pop(0)
    print(argumentos)
    for a in argumentos:
        caminho = os.path.abspath(a)
        reverse = []
        with open(caminho, "r", encoding="utf8") as file:
            for line in file:
                line = line.strip()
                print(line)

except FileNotFoundError:
    print("Não foi possivel encontrar o arquivo!")