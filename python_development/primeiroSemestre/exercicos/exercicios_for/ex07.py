#!/bin/python env

# 7 – Dada a base e o expoente, calcular a potencia.
# ENTRADA: 2  4 	SAÍDA: 16

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

potencia = 1

for turn in range(0, expoente, 1):
    potencia = potencia * base
print(f"{base} elevado a {expoente} é igual a {potencia}")


# expoente será a quantidade de vezes que o laço se repetirá.
# cada vez que o laço se repetir,a variavel potência, será
# substituída pelo novo valor
