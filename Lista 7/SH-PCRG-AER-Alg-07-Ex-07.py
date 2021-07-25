def gerar_cartela():
    dic = {"B": [],"I": [],"N": [],"G": [],"O": []}
    contador = 0
    for key in dic.keys():
        for x in range(1,6):
            dic[key].append(contador+1)
            contador+=1
        contador+=10
    print(dic)
    mostrar_cartela(dic)

def mostrar_cartela(dic):
    print(f'-------------------------------')
    print(f' B      I      N      G      O ')
    print(f'-------------------------------')
    for x in range(5):
        print(f' {dic["B"][x]}     {dic["I"][x]}     {dic["N"][x]}     {dic["G"][x]}     {dic["O"][x]}')
    print(f'-------------------------------')

gerar_cartela()


