import numpy

def triangulo_valido(l1,l2,l3):
    if ((numpy.abs(l1-l2))<l3<(l1+l2)):
       if ((numpy.abs(l1-l3))<l2<(l1+l3)):
          if ((numpy.abs(l3-l2))<l1<(l3+l2)):
            return True
    return False

def main():
  l1 = int(input("Qual o lado 1? "))
  l2 = int(input("Qual o lado 2? "))
  l3 = int(input("Qual o lado 3? "))

  print(f'{triangulo_valido(l1,l2,l3)}')

if __name__ == "__main__":
    main()