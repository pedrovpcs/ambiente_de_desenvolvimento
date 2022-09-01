#!/bin/env python

# 8. Dado um número pelo usuário, verifique se ele é “Positivo”, “Negativo” ou “Nulo”(igual a zero).
# Entrada: 3 Saída: Positivo
# Entrada: -5 Saída: Negativo
# Entrada: 0 Saída: Nulo

numero = int(input("Digite um número para a verificação: "))

if numero > 0:
    print("Número positivo.")
elif numero == 0:
    print("Número nulo.")
else:
    numero < 0
    print("Número negativo.")


# OUU...


# numero = int(input("Digite um número para a verificação: "))

# if numero >= 0:
#     if numero == 0:
#         print("Número nulo.")
#     else:
#         print("Número positivo.")
# else:
#     print("Número negativo.")
