def remover_extremos(listap,num_valores):
  lista_arrumada = listap.copy()
  lista_arrumada.sort()

  for x in range(num_valores):
    del lista_arrumada[0]
    del lista_arrumada[-1]

  return(lista_arrumada)

def main():
  lista = []
  while(True):
    num = int(input("Me dê um numero: "))
    if num == 0:
      break
    lista.append(num)
  if len(lista)<4:
    print("Me dê ao menos 4 valores.")
    return
  print(f'{remover_extremos(lista, 2)} - {lista}')

if __name__ == "__main__":
    main()