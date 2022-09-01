#!/bin/env python

# 1 - Preencher uma lista com dez elementos float.

lista = []
for i in range(10):
    x = input(f"Digite o elemento float: ")
    lista.append(x)
print(lista)

# "i" é o elemento e "range" irá mostrar até quantos elementos a lista irá conter (quantidade de vezes que o laço repetirá)
# "x" é o input do usuário para digitar elemento por elemento
# "lista.append()" acrescentará um elemento no final da lista
# "i" sempre começa no primeiro elemento da lista
