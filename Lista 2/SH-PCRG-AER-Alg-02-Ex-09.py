#Pedindo data no formato DDMMAA
data = int(input("Diga a data usando a formatação DDMMAA: "))

#Fazendo as operações para inverter a data.
anos = data%100
meses = (data%10000 - anos)//100
dias = (data - meses - anos)//10000

#Invertendo a data
datainvertida = anos * 10000 + meses *100+ dias

#Printando a data e comparando com a data invertida
print(f'Data = {data}\nData Invertida = {datainvertida}')

