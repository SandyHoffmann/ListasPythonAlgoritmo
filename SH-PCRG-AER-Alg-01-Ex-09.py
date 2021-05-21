#Pedindo valor inicial ao usuário
valor_inicial = float(input("Qual o valor inicial da conta? "))

#Calculando novos valores em 1, 2 e 3 anos
valor_ano1 = valor_inicial*1.12
valor_ano2 = valor_ano1*1.12
valor_ano3 = valor_ano2*1.12

#Mostrando valores no terminal
print(f'Valor investimento 1 ano: {valor_ano1:.2f}\nValor investimento 2 anos: {valor_ano2:.2f}\nValor investimento 3 anos: {valor_ano3:.2f}')
