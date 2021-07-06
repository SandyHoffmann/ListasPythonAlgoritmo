def remover_extremos(listap,num_valores):
  listap.sort()
  lista_ordenada = listap.copy()
  lista_arrumada = []
  for x in range(num_valores):
    listap.remove(x)
    listap.remove(len(listap)-x)

  return(listap)

def teste():
  lista = []
  while(True):
    num = int(input("Me dê um numero: "))
    if num == 0:
      break
    lista.append(num)
  if len(lista)<4:
    return("Me dê ao menos 4 valores.")
  print(lista)
  print(f'{remover_extremos(lista, 2)} - {lista}')

teste()