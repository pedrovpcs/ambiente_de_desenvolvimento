#!/bin/python env

# 7. Dada uma frase, exibir a ultima palavra.
# 	ENTRADA: estou gostando de string no python                      SAÍDA: python


frase = input("Digite uma frase:")
index_espaco = 0

for index in range(0, len(frase), 1):

    if frase[index] == " ":
        index_espaco = index

for index in range(index_espaco + 1, len(frase), 1):
    print(f"{frase[index]}", end="")

# a variavel "index" é reescrevida sempre que passa por um " ". Quando ela chega no último espaço, guarda o valor dele.
#
