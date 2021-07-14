def verifica_media(lista):
    totalResultado = []
    acima = []
    mediana = []
    abaixo = []
    media = sum(lista)/ len(lista)
    print(media)
    for i in lista:
        if int(i) < media:
            abaixo.append(i)
        if int(i) > media:
            acima.append(i)
    lista.sort()
    if len(lista)%2==0:
        mediana.append((lista[int(len(lista)/2)]+lista[int(len(lista)/2+1)])/2)
    else:
        mediana.append(lista[round(len(lista)/2)])
    totalResultado = [abaixo,mediana,acima]
    return totalResultado

def main():
    lista = []
    numero = "teste"
    while numero != "":
        numero = str(input("Digite um numero"))  
        if numero != "":
            lista.append(int(numero))
    
    resultado = verifica_media(lista)
    print(resultado)
    print(f'Abaixo: {resultado[0]}\nMédia: {resultado[1]}\Acima: {resultado[2]}')
    
if __name__ == "__main__":
    main()
