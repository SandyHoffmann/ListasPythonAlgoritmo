def hipotenusa(lado1,lado2):
  soma = lado1 ** 2 + lado2 **2
  hipotenusa = (soma)**(1/2)
  return(hipotenusa)

def main():
  lado1 = int(input("Qual o lado 1? "))
  lado2 = int(input("Qual o lado 2? "))
  print(f'A hipotenusa é: {hipotenusa(lado1,lado2)}')

if __name__ == "__main__":
    main()