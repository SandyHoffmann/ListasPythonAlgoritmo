totalbit = ""
while True:
    bit = input("Me de os bits. ")
    if bit == "":
        break
    totalbit+=bit

zeros = totalbit.count("0")
uns = totalbit.count("1")

if len(totalbit)!=8:
    print("Erro, n é uma sequencia de 8 bits! ")

elif uns%2==0:
    print("Adicionar 0")
else:
    print("Adicionar 1")