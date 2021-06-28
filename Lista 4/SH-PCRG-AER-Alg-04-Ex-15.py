result = ""
decimal = int(input("Me de um numero decimal: "))
numero = decimal
r = 0
while decimal!=0:
    r = decimal%2
    result=str(r) + result
    decimal = decimal//2

print(f'O numero foi de {numero} para {result}')