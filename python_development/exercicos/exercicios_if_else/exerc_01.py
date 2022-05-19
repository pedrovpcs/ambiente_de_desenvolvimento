#!/bin/env python

# 1. Dado um número pelo usuário, verificar se ele é positivo, exibindo a mensagem “O numero é
# positivo” ou “O numero não é positivo”.
# Entrada: 45 Saída: O numero é positivo
# Entrada: -3 Saída: O numero não é positivo
# Entrada: 0 Saída: O numero não é positivo

numero = int(input("Digite um número para verificar se é positivo ou negativo: "))

if numero > 0:
    print("O número é positivo.")
else:
    print("O número não é positivo. ")
