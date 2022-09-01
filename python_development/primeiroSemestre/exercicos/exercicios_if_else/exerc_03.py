#!/bin/env python

# 3. Dado um número pelo usuário, verificar se “O número é par” ou “O número é impar”,
# exibindo sua respectiva mensagem.
# Entrada: 3 Saída: O numero é impar
# Entrada: 10 Saída: O numero é par

numero = int(input("Digite um número para a verifição: "))

if numero % 2 == 0:
    print("Número par.")
else:
    print("Número ímpar.")
