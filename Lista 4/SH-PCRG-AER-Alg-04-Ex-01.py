#Declarando variaveis acumuladoras
soma = 0
contador = 0
#loop infinito
while (True):
    #perguntando valor x
    x = float(input("Mê de uma nota, quando quiser parar digite 0 :"))
    #se x for 0 quebra o loop
    if x == 0:
        break
    #colocando valores na soma, e tbm pegando as quantidades de notas
    soma+=x
    contador+=1
#mostrando na tela
print(f'A media total é de {soma/contador}')
