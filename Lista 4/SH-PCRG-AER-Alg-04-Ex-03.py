#Cabeçalho da tabela
print(f'Celcius    -    Fahrenheit')
#range de 100 graus (considerando 100)
for x in range (101):
    #Se for multiplo de 10
    if x%10 ==0:
        #Conta e bota na tabela.
        grausf = (x * 9/5) + 32
        print(f'{x} °C\t\t{grausf} °F')
