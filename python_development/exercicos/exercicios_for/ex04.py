#!/bin/python env

# 4 - Dados dois números, exibir os números do seu intervalo (não incluindo eles)
# ​ ENTRADA: 4  8​	SAÍDA:  5 6 7

number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))

for number in range(number1 + 1, number2, 1):
    print(number)
