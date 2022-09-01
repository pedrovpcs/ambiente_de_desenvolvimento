#!/bin/env python

# 7. Juntar os dois exercícios anteriores, ou seja, pedir a digitação das duas notas, caso uma (ou as duas)
# nota seja inválida exibir “Nota inválida!” e terminar o algoritmo; senão, calcular e exibir a média e
# exibir se está aprovado (vide saída do exercício anterior).
# Entrada: 10.0 4.0 Saída: 7.0 – Você está aprovado
# Entrada: 2.0 3.0 Saída: 2.5 – Você está reprovado
# Entrada: 14.0 Saída: Nota Inválida!
# Entrada: 5.0 -6.0 Saída: Nota Inválida!

nota1 = float(input("Digite a primeira nota: "))
if 0 <= nota1 <= 10:
    nota2 = float(input("Digite a segunda nota: "))
    if 0 <= nota2 <= 10:
        media_simples = (nota1 + nota2) / 2
        if media_simples < 5:
            print(f"{media_simples} - Você está reprovado! ")
        else:
            print(f"{media_simples} - Você está aprovado!")
    else:
        print("Nota inválida!")
else:
    print("Nota inválida! ")
