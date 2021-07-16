from postfixtoken import toToken,postfix
from precedenciapy import precedencia

def av_postfix(exp):
    lista = []
    for i in exp:
        if type(i) == int:
            lista.append(i)
        else:
            direita = lista[-1]
            lista.pop(-1)
            esquerda = lista[-1]
            lista.pop(-1)
            lista.append(str(direita)+str(i)+str(esquerda))
    
    return lista

def main():
  token = input("Dê-me um token: ")
  print(av_postfix(postfix(toToken(token))))
  
if __name__ == "__main__":
    main()