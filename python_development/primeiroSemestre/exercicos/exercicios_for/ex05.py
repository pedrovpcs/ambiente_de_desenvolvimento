#!/bin/python env

# 5 - Dado um número, verificar se ele é primo ou não
# ENTRADA: 11	SAÍDA: É primo

num = int(input("Digite um número: "))
num_multiplos = 0
lista_multiplos = []
primo = False

for numero in range(1, num + 1, 1):
    if num % numero == 0:
        num_multiplos += 1
        lista_multiplos.append(numero)

if len(lista_multiplos) == 2:
    primo = True

print(f"Os multiplos do número {num} são: ", end="")
for numero in lista_multiplos:
    print(numero, end=" ")

print()
if primo:
    print("E ele é primo")
else:
    print("E ele não é primo")
