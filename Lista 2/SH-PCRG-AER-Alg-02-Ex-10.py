#Pedindo matricula
data = int(input("Diga a matricula usando a formatação AASDDD: "))

#Pegando o ano
ano = data//10000

#Pegando o semestre 
semestre = data//1000 - ano*10

#Mostrando no console
print(f'Ano: {ano}, Semestre: {semestre}')
