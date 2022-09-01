#!/bin/python env

# V3. Somar números até que seja digitado um numero negativo. O numero negativo não fará parte da somatória.
# ENTRADA: 7 2 10 20 1 -5		SAÍDA: 40

number = 0  # nunca se esquecer de definir a variável condicional para entrar no laço
soma = 0  # nunca se esquecer de definir a variável acumuladora/contadora antes de começar o laço
while number >= 0:
    number = int(input("Digite números para serem somados: "))
    soma += number
print(soma)
