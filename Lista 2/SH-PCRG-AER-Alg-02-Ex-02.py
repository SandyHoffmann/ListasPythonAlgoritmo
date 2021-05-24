#Pegando dados de segundos.
segundos = int(input("Quantidade de segundos: "))

#Convertendo os segundos para seus respectivos dias, horas e minutos 
dias = segundos//86400
horas = (segundos-(dias*86400))//3600
minutos = (segundos-(dias*86400)-(horas*3600))//60
segundos = (segundos-(dias*86400)-(horas*3600))%60

#Mostrando no console, formatando de acordo com o pedido com a questão
print(str(dias)+':'+'{:0>2}'.format(horas)+':'+'{:0>2}'.format(minutos)+':'+'{:0>2}'.format(segundos))