#!/bin/env python

# COLA

# for numero in range(0, 10, 1):  o primeiro número será onde dará início a contagem (incluindo ele mesmo),
#     print(numero)               o segundo número será onde a contagem terminará (sem incluir o número escolhido/um
#                                 número antes do escolhido),
#                                 e o terceiro número indicará se a contagem será crescente ou decrescente e
#                                 de quantos em quantos números.
#
#                                           Exemplo: -1 seria decrescente de 1 em 1.
#                                           1 seria crescente de 1 em 1

# EXERCÍCIOS:
# 1- Dado um número, exibir os seus próximos 10 números
# ENTRADA: 10	SAÍDA: 10 11 12 13 14 15 16 17 18 19

n = int(input("Digite um numero: "))

for cont in range(n + 1, n + 10, 1):
    print(cont)
