#!/bin/env python

# 5. Dadas duas notas, calcular e exibir a média simples das mesmas. Caso a média seja inferior a 5
# exibir “Você está reprovado”, senão exibir “Você está aprovado”.
# Entrada: 7.0 5.0 Saída: 6.0 – Você está aprovado
# Entrada: 4.5 3.5 Saída: 4.0 – Você está reprovado

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media_simples = (nota1 + nota2) / 2

if media_simples < 5:
    print(f"{media_simples} - Você está reporvado.")
else:
    print(f"{media_simples} - Você está aprovado.")
