#Pedindo mês e fazendo com q ele sempre fique no formato minusculo.
mes = input("Qual o mês? ").lower()
#Checando os meses para printar o tanto de dias.
if mes == "janeiro":
    print(f'O mês de {mes} tem 31 dias.')
elif mes == "fevereiro":
    print(f'O mês de {mes} tem 28 ou 29 dias.')
elif mes == "março":
    print(f'O mês de {mes} tem 31 dias.')
elif mes == "abril":
    print(f'O mês de {mes} tem 30 dias.')
elif mes == "maio":
    print(f'O mês de {mes} tem 31 dias.')
elif mes == "junho":
    print(f'O mês de {mes} tem 30 dias.')
elif mes == "julho":
    print(f'O mês de {mes} tem 31 dias.')
elif mes == "agosto":
    print(f'O mês de {mes} tem 31 dias.')
elif mes == "setembro":
    print(f'O mês de {mes} tem 30 dias.')
elif mes == "outubro":
    print(f'O mês de {mes} tem 31 dias.')
elif mes == "novembro":
    print(f'O mês de {mes} tem 30 dias.')
elif mes == "dezembro":
    print(f'O mês de {mes} tem 31 dias.')
#Se n for encontrado retorna uma mensagem de erro.
else:
    print("Não foi encontrado mês com esse nome.")