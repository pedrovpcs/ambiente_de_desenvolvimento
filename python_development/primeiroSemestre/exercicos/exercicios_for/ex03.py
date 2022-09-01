#!/bin/python env

# 3 - Dados dois números, exibir os números do seu intervalo (incluindo eles)
# ENTRADA: 4  8​	SAÍDA: 4 5 6 7 8

number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))

for number in range(number1, number2 + 1, 1):
    print(number)
