#Pedindo numero
numero = int(input("Diga um numero de 3 digitos: "))

#Fazendo as operações para separar as centenas, dezenas e unidades.
centenas = numero //100
dezenas = (numero  - (centenas*100))//10
unidades = (numero - (centenas*100) - (dezenas*10))//1

#Printando as divisões na tela
print(f'Centenas = {centenas}')
print(f'Dezenas = {dezenas}')
print(f'Unidades = {unidades}')

