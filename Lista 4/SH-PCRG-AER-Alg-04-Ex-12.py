print("\t 1\t 2\t 3\t 4\t 5\t 6\t 7\t 8\t 9\t 10\t")
linhas = [[],[],[],[],[],[],[],[],[],[]]
for x in range(10):
    linha = f"{x+1}"
    atual = 0
    for y in range(11):
        if y == 0:
            inicial = x+1
            linhas[x].append(inicial)
        else:
            atual += x+1
            linhas[x].append(atual)

for elemento in linhas:
    linha = "\n"
    for x in elemento:
        linha+='\t'+ str(x)
    print(linha)