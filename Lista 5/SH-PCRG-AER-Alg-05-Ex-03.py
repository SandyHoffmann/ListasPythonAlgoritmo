def calcular_envio(quantidade):
  valor = 10.95 + ((quantidade-1)*2.95)
  return(valor)

def main():
  quantproduto = int(input("Qual é a quantidade de itens? "))
  print(f'O valor total é de: {calcular_envio(quantproduto)}')

if __name__ == "__main__":
    main()