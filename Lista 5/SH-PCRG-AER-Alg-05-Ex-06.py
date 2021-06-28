def centralizando_palavra(string,largura):
    largura_metade=largura//2
    return(" "*largura_metade + string)

def main():
  string = input("Qual é a palavra? ")
  largura = int(input("Qual o espaçamento?"))
  print(f'{centralizando_palavra(string,largura)}')

if __name__ == "__main__":
    main()