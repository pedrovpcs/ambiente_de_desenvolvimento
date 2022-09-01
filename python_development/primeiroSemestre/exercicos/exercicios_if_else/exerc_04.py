#!/bin/env python

# 4. Dados dois números pelo usuário, exibir o de maior valor.
# Entrada: 5 45 Saída: 45
# Entrada: 10 8 Saída: 10

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O maior número é: {num1}")
else:
    print(f"O maior número é {num2}")
