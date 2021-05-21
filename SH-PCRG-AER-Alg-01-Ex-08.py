#Pedindo a quantidade
bugiganga = int(input("Quantas bugigangas você quer? "))
quinquilharia = int(input("Quantas quinquilharias você quer? "))

#Calculando peso de cada artigo
peso_bugiganga = bugiganga * 75
peso_quinquilharia = quinquilharia * 112

#Somando para obter o peso total do pedido
peso_total_pedido = peso_bugiganga + peso_quinquilharia

#Mostrando peso total para usuário
print(f'O peso total do seu pedido é de {peso_total_pedido} gramas.')
