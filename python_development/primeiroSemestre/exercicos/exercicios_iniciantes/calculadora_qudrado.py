#!/bin/env python

# Exercício 2. Dado um numero pelo usuário, calcular o quadrado
# Entrada: 3    Saída: 9

n1 = input("Digie o número quer saber o quadrado: ")
n1 = float(n1)
r1 = n1 * n1
print(f"Esse número elevado ao quadrado é:{r1}\n")
print("Esse número elevado ao quadrado é: %s \n" % r1)  # outra forma possível...
print("Esse número elevado ao quadrado é: {}".format(r1))
texto = "Esse número elevado ao quadrado é: {} "  #
print(texto.format(r1))  # "texto" foi substituído para facilitar nessa linha
