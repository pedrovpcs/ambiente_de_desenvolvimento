#!/bin/env python

# 2. Dada uma mensagem e a quantidade de vezes, exibi-la na tela
#   ENTRADA: oi 4      SAÍDA: oi oi oi oi

message = input("Digite uma mensagem: ")
times_repeated = int(input("Digite a quantidade de vezes que a menssagem será repetida: "))
turn = 1

while turn <= times_repeated:
    print(f"{message}")
    turn += 1