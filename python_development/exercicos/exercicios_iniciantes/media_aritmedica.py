#!/bin/env python

# 6. Fazer um algoritmo que calcule a média de 4 números dados pelo usuário.
# Entrada:	1 4 6 2 Saída:	3.25
# Entrada:	6 0 5 8 Saída:	4.75

n1 = input("Digite o primeiro número: ")
n1 = float(n1)
n2 = input("Digite o segundo número: ")
n2 = float(n2)
n3 = input("Digite o terceiro número: ")
n3 = float(n3)
n4 = input("Digite o quarto número: ")
n4 = float(n4)
r1 = (n1 + n2 + n3 + n4) / 4
print(f"A média aritmédica é de: {r1}\n")
