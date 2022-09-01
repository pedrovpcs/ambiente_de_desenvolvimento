#!/bin/env python


# 5. Crie uma função que retorne o maior entre dois números passados por parâmetro
# protótipo: maior_2n(15,98)
# Retorno: 98


def maior_2n(x, y):
    if x > y:
        return x
    else:
        return y


z = maior_2n(14, 2)
print(z)
