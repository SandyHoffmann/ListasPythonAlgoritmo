import os
import sys

try:
    x = 0
    caminho = os.path.abspath(f'{sys.argv[1]}')
    reverse = []
    with open(caminho, "r", encoding="utf8") as file:
        for line in reversed(list(file)):
            line = line.strip()
            reverse.append(line)
            x+=1
            if x>9:
                break
    print(reverse) 

except FileNotFoundError:
    print("Não foi possivel encontrar o arquivo!")
