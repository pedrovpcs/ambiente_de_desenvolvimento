#!/bin/env python

# EXERCÍCIOS:
# 1- Dado um número, exibir os seus próximos 10 números
# ENTRADA: 10	SAÍDA: 10 11 12 13 14 15 16 17 18 19

n = int(input("Digite um numero: "))

for cont in range(n + 1, n + 10, 1):
    print(cont)
