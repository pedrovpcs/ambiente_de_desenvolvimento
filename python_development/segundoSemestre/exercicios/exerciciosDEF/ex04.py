#!/bin/env python

# 4. Crie uma função que retorne o proximo número ao passado por parâmetro.
# protótipo: prox_num(5)
# Retorno: 6


def prox_num(numero):
    numero += 1
    return numero


num = prox_num(5)
print(num)
