def elimina_simbolos(string):
    simbolos_eliminar = ["?", ",",".","!"]
    for s in simbolos_eliminar:
        string = string.replace(s,"")
    return string.split(" ")

def main():
    frase = input("Me de uma frase: ")
    print(elimina_simbolos(frase))
if __name__ == "__main__":
    main()


