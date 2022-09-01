#!/bin/python env

# 7 - Exibir apenas os elementos negativos

lista = [2.3, -1.5, 4.6, -7.8, 9.5, 8.2, -0.7, 6.4, 3.2, 0.2]

for i in range(10):
    if lista[i] < 0:  # aqui ocorre a verificação se o número é negativo
        print(
            lista[i]
        )  # mais uma vez "lista[i]" verificando cada elemento na lista e acatando a regra do "if"
