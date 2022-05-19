#!/bin/env python

# 7. Dada a quilometragem parcial de um carro e a quantidade de litros gastos por um carro
# para percorrer esta quilometragem, fazer um algoritmo que calcule quantos Km/l o
# carro percorreu.
# Entrada:	345.6 25.4 Saída:	13.6
# Entrada:	556.1 59.7 Saída:	9.31

distance = input("Digite a quilometragem percorrida: ")  # em km
distance = float(distance)
fuel_amount = input("Digite a quantidade de litros gastos: ")  # em litros
fuel_amount = float(fuel_amount)
efficiency = distance / fuel_amount
print(
    f"O carro percorreu {efficiency:.2f} Km/l"
)  # ":.2f" indica as casas decimais aparentes depois da "virgula"
