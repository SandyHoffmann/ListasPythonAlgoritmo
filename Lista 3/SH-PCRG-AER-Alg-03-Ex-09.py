#Perguntando mês e dia
mes = input("Qual o mês? ").lower()
dia = int(input("Qual o dia? "))

#Montando as condições e informando os feriados.
if dia == 1:
    if mes == "janeiro":
        print("Confraternização universal")
    elif mes == "maio":
        print("Dia do trabalho")

elif mes == "abril" and dia == 21:
    print("Tiradentes")

elif mes == "setembro" and dia == 7:
    print("Independência do Brasil")

elif mes == "outubro" and dia == 12:
    print("Nossa Senhora Aparecida")

elif mes == "novembro":
    if dia == 2:
        print("Finados")
    if dia == 15:
        print("Proclamação da República")

elif mes == "dezembro" and dia ==25:
    print("Natal")
#Caso os feriados não sejam achados ele retorna que não encontrou.
else:
    print("O dia e o mês informados não correspondem a um feriado nacional.")
