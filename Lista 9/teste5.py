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
            reverse = []
            with open(caminho, "r", encoding="utf8") as file:
                for line in file:
                    contador += 1
                    line = f'{contador}: {line.rstrip()}\n'
                    outfile.write(line)

except FileNotFoundError:
    print("Não foi possivel encontrar o arquivo!")
