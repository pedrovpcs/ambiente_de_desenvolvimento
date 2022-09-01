#!/bin/env python

# 6. Crie uma função que retorne o maior entre três números passados por parâmetro
# protótipo: maior_3n(115,23,8)
# Retorno: 115

"""
def maior_3n(x, y, z):
    if (x > y) and (x > z):
        return x
    elif (y > x) and (y > z):
        return y
    else:
        return z
"""
# ou...


def maior_3n(n1, n2, n3):
    maior = n1
    if n2 > maior:
        maior = n2

    if n3 > maior:
        maior = n3

    return maior


b = maior_3n(7, 115, 8)
print(b)
