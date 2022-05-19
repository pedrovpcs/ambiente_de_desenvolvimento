#!/bin/env python


# 10. Dada a quantidade de minutos, fazer um algoritmo que calcule quantas horas e
# minutos este tempo compõe.
# Entrada: 150 Saída: 2h30m

minute = input("Digite os minutos: ")
minute = int(minute)
hour = minute // 60
minute = minute % 60


print(f"{hour} horas e {minute} minutos")
