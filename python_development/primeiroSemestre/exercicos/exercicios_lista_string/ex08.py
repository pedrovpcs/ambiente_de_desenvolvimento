#!/bin/python env

# 8. Dada uma frase, contar a quantidade de palavras
# 	ENTRADA: estou gostando de string no python                      SAÍDA: 6

frase = input("Digite uma frase:").strip()
cont_espaco = 0

for letra in frase:
    if letra == " ":
        cont_espaco += 1

print(f"A quantidade de palavras é {cont_espaco + 1}")
