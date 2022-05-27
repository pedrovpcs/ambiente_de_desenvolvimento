#!/bin/python env


# 4. Dada uma letra, contar quantos caracteres existem na frase.
# 	ENTRADA: boa noite | o               SAÍDA: 2


achaLetra = input("Digite um letra: ")
frase = input("Digite uma frase: ")
cont = 0
for letra in frase:
    if letra == achaLetra:
        cont += 1
print(f"Na frase: '{frase}' foi encontrado {cont}x a letra '{achaLetra}'")


# a variavel "letra", "escaneia" a frase digitada e sempre q a letra q o usuario digitou é encontrada, a variavel contadora (cont) soma + 1
