#linha com preços
precosiniciais = [4.95,9.95,14.95,19.95,24.95]
#range para os 5 valores
for x in range(5):
    # calculando valores
    valorcomdesconto = precosiniciais[x]*0.60
    desconto = precosiniciais[x] - valorcomdesconto
    # se for 0 ele bota o cabeçalho da tabela
    if x == 0:
        print(f'Valor inicial - Desconto - Valor Final')
    # printando os valores da tabela
    print(f'{precosiniciais[x]:.2f} \t\t |{desconto:.2f}\t\t| {valorcomdesconto:.2f}')