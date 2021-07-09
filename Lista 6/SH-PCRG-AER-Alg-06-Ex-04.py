lista = []
while (True):
    info = input("Digite algo:")
    if info == "":
        break
    lista.append(info)

lista_copia = lista.copy()
lista_rem = []

for x in range(len(lista)):
    contador = 0
    for y in range(len(lista)):
        if lista[x] == lista[y]:
            if contador>0:
                if y in lista_rem:
                    pass
                else:
                    lista_rem.append(y)
            else:
                contador+=1
print(lista_rem)
novo_ind = 0
lista_rem.sort()
for i in lista_rem:
    del lista[i-novo_ind]
    novo_ind+=1

print(lista)

