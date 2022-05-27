#!/bin/python env

# 6 - Dado um numero, calcular o seu fatorial. (Ex: 4! = 4 . 3 . 2 . 1 = 24)
# ENTRADA: 3	SAÍDA: 6

number1 = int(input("Digite um número para calcular seu fatorial: "))

fatorial = 1

for turn in range(number1, 0, -1):
    fatorial = fatorial * turn
print(fatorial)

# sempre antes do programa entrar no laço, ele subtrai 1 de "turn" e depois realiza a operação
# quando chega ao destino (zero nesse caso), o laço termina e o resultado de tds as multiplicações é mostrado
# fatorial é uma variével contadora, por tanto utiliza ela mesma no cálculo
# operando com uma constante
