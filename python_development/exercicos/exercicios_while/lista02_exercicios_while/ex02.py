#!/bin/env python

# 2. Somar números até que seja digitado zero
# ENTRADA: 4 6 9 3 0		SAÍDA: 22


# V2. Somar números até que seja digitado um numero negativo
# ENTRADA: 10 22 1 -3		SAÍDA: 30


# V3. Somar números até que seja digitado um numero negativo. O numero negativo não fará parte da somatória.
# ENTRADA: 7 2 10 20 1 -5		SAÍDA: 40


n1 = int(input("Digite o número: "))
if n1 == 0:
    print("0")
else:
    soma = 0
    while n1 != 0:
        soma = soma + n1
        n1 = int(input("Digite o número: "))
    print(f"{soma}")
