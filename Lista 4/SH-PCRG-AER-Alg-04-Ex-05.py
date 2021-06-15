conta = 0
#loop infinito
while (True):
    #perguntando as idades
    idades = (input("Mê de as idades: "))
    #vendo se idades é vazio
    if idades == "":
        break
    idadealvo = int(idades)
    #fazendo a conta total
    if idadealvo<3:
        pass
    elif idadealvo<13:
        conta+=14
    elif idadealvo<64:
        conta+=18
    else:
        conta+=23

#mostrando na tela
print(f'Deu um total de {conta:.2f} reais.')
