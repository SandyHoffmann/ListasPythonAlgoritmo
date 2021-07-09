lista = []
def verifica_int(num):
    try:
        int(num)
    except ValueError:
        return False
    return True

while (True):
    info = input("Digite um número inteiro:")
    if info == "":
        break
    if verifica_int(info):
        lista.append(int(info))

for elemento in lista:
    if elemento<0:
        print(elemento)

for elemento in lista:
    if elemento ==0:
        print(elemento)

for elemento in lista:
    if elemento>0:
        print(elemento)

