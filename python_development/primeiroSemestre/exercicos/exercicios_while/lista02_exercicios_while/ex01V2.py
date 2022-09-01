#!/bin/python env

# V2. Exibir em formato de tabuada
# ENTRADA: 3      SAÍDA:  3 X 1 = 3
#             3 X 2 = 6
#             ...
#             3 X 10 = 30

n1 = int(input("Digite o número que deseja saber a tabuada: "))
turn = 1

while turn <= 10:
    multiplex = turn * n1
    print(f"{n1} X {turn} = {multiplex}")
    turn += 1
