n = int(input("Me de uma raiz: "))
raiz = n
while abs(n - (raiz*raiz)) > (10 ** -12):
    raiz = (raiz + (n/raiz))/2

print(f'A raiz em questão é: {raiz}')