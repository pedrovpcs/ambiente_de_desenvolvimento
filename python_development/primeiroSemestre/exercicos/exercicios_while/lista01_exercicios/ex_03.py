#!/bin/env python

# # 3. Dado um número, exibir os seus  próximos 5 multiplos (contando ele)
# #   ENTRADA: 2      SAÍDA: 2 4 6 8 10

n1 = int(input("Digite o número que deseja exibir os próximos 5 multiplos: "))
turn = 1
while turn <= 5:
    multiplex = n1 * turn
    print(multiplex)
    turn += 1
