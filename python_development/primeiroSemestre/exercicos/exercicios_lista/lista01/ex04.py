#!/bin/python env

# 4 - Calcular a média dos elementos

lista = [2.3, 1.5, 4.6, 7.8, 9.5, 8.2, 0.7, 6.4, 3.2, 0.2]
soma = 0
for i in range(10):
    soma += lista[
        i
    ]  # como a variavel contadora é igual a zero, ela ira sempre acumular e somar o elemnetos na lista

media = soma / (
    i + 1
)  # nunca se esquecer dos parenteses!  # i + 1 é o numero maximo de elementos dentro da lista + 1, pois sempre se começa no zero
print(media)
