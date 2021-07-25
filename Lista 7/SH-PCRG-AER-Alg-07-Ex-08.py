def gerar_cartela():
    dic = {"B": [],"I": [],"N": [],"G": [],"O": []}
    for key in dic.keys():
        for x in range(1,6):
            num = int(input(f'Numero para {key}: '))
            dic[key].append(num)
    print(dic)
    print(conferir_cartela(dic))

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

def main():
    dic_linha = {'B': [1, 1, 1, 1, 1], 'I': [8, 8, 8, 
                8, 8], 'N': [0, 0, 0, 0, 0], 'G': [8, 
                8, 8, 8, 8], 'O': [8, 8, 8, 8, 8]} 
    dic_col = {'B': [1, 0, 1, 1, 1], 'I': [1, 0, 1, 
                1, 1], 'N': [1, 0, 1, 1, 1], 'G': [1, 
                0, 1, 1, 1], 'O': [1, 0, 1, 1, 1]}  
    dic_diag = {'B': [0, 1, 1, 1, 1], 'I': [1, 0, 1, 
                1, 1], 'N': [1, 1, 0, 1, 1], 'G': [1, 
                1, 1, 0, 1], 'O': [1, 1, 1, 1, 0]} 
    dic_diag_rev = {'B': [1, 1, 1, 1, 0], 'I': [1, 1, 1, 
                    0, 1], 'N': [1, 1, 0, 1, 1], 'G': [1, 
                    0, 1, 1, 1], 'O': [0, 1, 1, 1, 1]} 
    dic_errado = {'B': [0, 1, 1, 1, 0], 'I': [1, 1, 1, 
                    1, 1], 'N': [0, 1, 1, 0, 1], 'G': [1, 
                    1, 0, 1, 1], 'O': [1, 1, 1, 1, 1]}  
    print(f'Linha = {conferir_cartela(dic_linha)}')
    print(f'Coluna = {conferir_cartela(dic_col)}')
    print(f'Diagonal = {conferir_cartela(dic_diag)}')
    print(f'Diagonal Reversa = {conferir_cartela(dic_diag_rev)}')
    print(f'Errado = {conferir_cartela(dic_errado)}')

    #Para testes de tabelas
    # gerar_cartela()

if __name__ == "__main__":
    main()




