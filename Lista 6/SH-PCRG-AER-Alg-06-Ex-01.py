lista = []

while(True):
  num = int(input("Me dê um numero: "))
  if num == 0:
    break
  lista.append(num)

lista.sort()

for e in lista:
  print(e)