#!/bin/env python

# 6. Dada uma nota, verificar se ela é válida, ou seja, se ela estiver entre 0 e 10 (inclusive) ela é uma
# “Nota válida”, senão “Nota inválida”.
# Entrada: 3.5 Saída: Nota válida
# Entrada: 11.5 Saída: Nota Inválida

nota = float(input("Digite a nota para verificação: "))

if 0 <= nota <= 10:
    print("Nota válida!")
else:
    print("Nota inválida!")
