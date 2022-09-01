#!/bin/env python

# 8. Crie uma função que retorne o próximo numero multiplo N tomando como base o que foi passado por parâmetro.
# N Tambem deve ser pasado por parâmetro.
# protótipo: prox_multn(7,17)
# Retorno: 21


def prox_multn(mult, n):
    return n // mult * mult + mult


z = prox_multn(9, 77)
print(z)
