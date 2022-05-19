#!/bin/python env

# 2- Dado um número, exibir os seus 10 números anteriores (decrescente)
# ENTRADA: 10	SAÍDA: 10 9 8 7 6 5 4 3 2 1

n = int(input("Digite um número: "))

for cont in range(n, n - 10, -1):
    print(cont)
