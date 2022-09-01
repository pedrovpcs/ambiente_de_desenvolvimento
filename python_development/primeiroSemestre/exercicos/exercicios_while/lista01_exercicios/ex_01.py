#!/bin/env python

# 1. Dada uma mensagem pelo usuário, exibí-la 10x
#   ENTRADA: oi        SAÍDA: oi oi oi oi oi oi oi oi oi oi


message = input("Digite uma menssagem: ")
turn = 1
while turn <= 10:
    print(f"{message}")
    turn += 1
