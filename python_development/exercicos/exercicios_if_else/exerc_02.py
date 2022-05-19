#!/bin/env python

# 2. Dada uma idade pelo usuário, verificar e exibir a mensagem “Você é menor de Idade” ou “Você é
# maior de Idade”.
# Entrada: 15 Saída: Você é menor de Idade
# Entrada: 33 Saída: Você é maior de Idade

idade = int(input("Digite sua idade:  "))

if idade > 18:
    print("Você é maior de idade: ")
else:
    print("Você é menor de idade.")
