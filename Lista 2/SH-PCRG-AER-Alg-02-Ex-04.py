#Pedindo 3 numeros
num_1 = int(input("Me dê o primeiro número: "))
num_2 = int(input("Me dê o segundo número: "))
num_3 = int(input("Me dê o terceiro número: "))

#Achando maior, menor e o número do meio.
maior = max(num_1, num_2, num_3)
menor = min(num_1, num_2, num_3)
meio = (num_1+num_2+num_3)-maior-menor

#Mostrando eles em ordem
print(f'{menor} - {meio} - {maior}')