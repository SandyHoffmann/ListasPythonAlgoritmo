import os
import sys
try:
    caminho = os.path.abspath(f'{sys.argv[1]}')
    files = open(caminho,"r")
    x = 0
    for line in files:
        print(f'{line.rstrip()} ---')
        x+=1
        if x>11:
            break
    print()
except FileNotFoundError:
    print("Não foi possivel encontrar o arquivo!")

