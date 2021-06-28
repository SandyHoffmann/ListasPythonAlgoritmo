def ordinal(numero):
    if (numero == 1):
        return("Primeiro")
    elif (numero == 2):
        return("Segundo")
    elif (numero == 3):
        return("Terceiro")
    elif (numero == 4):
        return("Quarto")
    elif (numero == 5):
        return("Quinto")
    elif (numero == 6):
        return("Sexto")
    elif (numero == 7):
        return("Sétimo")
    elif (numero == 8):
        return("Oitavo")
    elif (numero == 9):
        return("Nono")
    elif (numero == 10):
        return("Décimo")
    elif (numero == 11):
        return("Décimo Primeiro")
    elif (numero == 12):
        return("Décimo Segundo")
    else:
        return("")

def main():
  numero = int(input("Qual é o número? "))
  print(f'O valor ordinal referente a {numero}: {ordinal(numero)}')

if __name__ == "__main__":
    main()