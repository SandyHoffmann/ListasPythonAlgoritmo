#Pedindo n
n = int(input("Diga um numero de 3 digitos: "))

#Fazendo as operações para separar as centenas, dezenas e unidades.
centenas = n //100
dezenas = (n  - (centenas*100))//10
unidades = (n - (centenas*100) - (dezenas*10))//1

#Formando M para ser o inverso de N
m = unidades*100 + dezenas*10 + centenas

#Printando o N e o M 
print(f'N = {n}\nM = {m}')

