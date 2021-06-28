cont = 0
binario = (input("Me de um numero: "))
numero = 0

tamanho = len(binario)
for elemento in binario:
    cont+=1
    numero+=(int(elemento)*(2 ** (tamanho - cont)))
print(f'O numero {binario} fica em decimal como {numero}')