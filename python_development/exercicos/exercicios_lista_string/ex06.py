#!/bin/python env

# 6. Dada uma frase, exibir a primeira palavra.
# 	ENTRADA: estou gostando de string no python                      SAÍDA: estou

frase = input("Digite uma frase: ")
palavra1 = " "
for letra in frase:
    if letra != " ":
        palavra1 += letra
    else:
        break
print(palavra1)