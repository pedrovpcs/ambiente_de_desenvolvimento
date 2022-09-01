#!/bin/env python


# 7. Crie uma função que retorne o próximo numero multiplo 5 tomando como base o que foi passado por parâmetro.
# protótipo: prox_mult5(13)
# Retorno: 15

"""
def prox_mult5(n):
    prox = n // 5 * 5 + 5
    return prox
"""

# ou...


def prox_mult5(n):
    return n // 5 * 5 + 5


z = prox_mult5(47)
print(z)
