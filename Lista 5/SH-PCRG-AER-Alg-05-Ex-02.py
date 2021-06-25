def taxi(distancia):
  metros = distancia//140
  valor = 4 + (0.25*metros)
  return(valor)

def main():
  distancia = float(input("Qual é a distância? "))
  print(f'O valor total é de: {taxi(distancia)}')

if __name__ == "__main__":
    main()