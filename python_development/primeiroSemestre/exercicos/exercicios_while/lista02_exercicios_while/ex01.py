#!/bin/env python

# 1. Dado um número, exibir os seus 10 primeiros múltiplos
# ENTRADA: 2      SAÍDA: 2 4 6 8 10 12 14 16 18 20


n1 = int(input("Digite o número: "))
turn = 1
while turn <= 10:
    multiplex = n1 * turn
    print(multiplex)
    turn = turn + 1
