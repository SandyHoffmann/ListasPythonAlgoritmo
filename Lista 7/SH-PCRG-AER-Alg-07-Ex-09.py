import random

def gerar_cartela():
    dic = {"B": [],"I": [],"N": [],"G": [],"O": []}
    valor_pos = [[1,15],[16,30],[31,45],[46,60],[61,75]]
    cont_p_k = 0
    num_sorteados = []
    for key in dic.keys():
        for x in range(1,6):
            if len(num_sorteados)==0:
                num = random.randint(valor_pos[cont_p_k][0],valor_pos[cont_p_k][1])
                dic[key].append(num)
                num_sorteados.append(num)
            else:
                flag = False
                while flag == False:
                    cont_rep = 0
                    num = random.randint(valor_pos[cont_p_k][0],valor_pos[cont_p_k][1])
                    for e in num_sorteados:
                        if num == e:
                            cont_rep+=1
                    if cont_rep == 0:
                        flag = True
                dic[key].append(num)
                num_sorteados.append(num)
        cont_p_k += 1
    for key in dic.keys():
        dic[key].sort()
    return(dic)
LISTA = []
def sorteio():
    lista_escolhas = []
    cartela = gerar_cartela()
    qt_n_sort = 0
    for x in range(1,76):
        lista_escolhas.append(x)
    flag = False
    while flag == False:
        random.shuffle(lista_escolhas)
        numero_esc = lista_escolhas[0]
        del lista_escolhas[0]
        for key in cartela.keys():
            if numero_esc in cartela[key]:
                qt_n_sort+=1
                for x in range(5):
                    if cartela[key][x] == numero_esc:
                        cartela[key][x] = 0
                        flag = conferir_cartela(cartela)
    LISTA.append(qt_n_sort)

def conferir_cartela(cartela):
    linhas = [[],[],[],[],[]]
    for key in cartela.keys():
        num_ant_colunas = 0
        for x in range(5):
            linhas[x].append(cartela[key][x])
            num_ant_colunas+=cartela[key][x]
        if num_ant_colunas == 0:
            return True
    soma_colunas = 0
    soma_colunas_rev = 0
    contador = 0
    contador_rev = 4
    for linha in linhas:
        soma_linhas = 0
        soma_colunas+=linha[contador]
        soma_colunas_rev+=linha[contador_rev]
        for x in range(5):
            soma_linhas+=linha[x]
        contador+=1
        contador_rev-=1
        if soma_linhas == 0:
            return True
    if soma_colunas == 0 or soma_colunas_rev==0:
        return True
    return False

def mostrar_cartela(dic):
    print(f'-------------------------------')
    print(f' B      I      N      G      O ')
    print(f'-------------------------------')
    for x in range(5):
        print(f' {dic["B"][x]}     {dic["I"][x]}     {dic["N"][x]}     {dic["G"][x]}     {dic["O"][x]}')
    print(f'-------------------------------')


def main():
    for x in range(1000):
        sorteio()
    minimo = LISTA[0]
    maximo = 0
    soma = 0
    for x in LISTA:
        soma+=x
        if x>maximo:
            maximo = x
        if x<minimo:
            minimo = x
    media = soma/1000
    print(f'O max foi {maximo} - O min foi {minimo} - A media foi {media}')

if __name__ == "__main__":
    main()




