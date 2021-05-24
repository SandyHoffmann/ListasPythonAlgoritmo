import math

#Pedindo a e b
a = int(input("Me diga valor 'a': "))
b = int(input("Me diga valor 'b': "))

#Efetuando contas
soma = a + b
diferença = b - a
produto = a*b
quociente = a/b
resto = a%2
log = math.log10(a)
exponencial = a**b

#mostrando no terminal
print("+----------------------------+")
print(f'|Soma        | {soma}')
print(f'|diferença   | {diferença}')
print(f'|produto     | {produto}')
print(f'|quociente   | {quociente}')
print(f'|resto       | {resto}')
print(f'|log         | {log:.5f}')
print(f'|exponencial | {exponencial}')
print("+----------------------------+")
