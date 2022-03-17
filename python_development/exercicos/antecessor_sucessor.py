#!/bin/env python

# Exercício 3. Dado um numero pelo usuário, exibir o anterior e posterior
# Entrada: 23    Saída: 22 24
 
n1 = input("Digite um número para saber seu antecessor e sucessor: ")
n1 = int(n1)
r1 = (n1-1)
r2 = (n1+1)
print(f"O antecessor deste número é {r1} e o sucessor é {r2}\n")