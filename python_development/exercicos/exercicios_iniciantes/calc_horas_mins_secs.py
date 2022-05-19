#!/bin/python env


# 11. Dada a quantidade de segundos, fazer um algoritmo que calcule quantas horas,
# minutos e segundos este tempo compõe.
# Entrada: 4000 Saída: 1h06m40s


second = input("Digite os segundos: ")
second = int(second)

hour = second // 60 // 60
minute = second // 60 % 60
second = second % 60 % 60

print(f"{hour} hora(s), {minute} minuto(s) e {second} segundo(s).")
