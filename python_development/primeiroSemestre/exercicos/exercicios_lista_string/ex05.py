#!/bin/python env

# 5. Dada uma frase, contar quantas vogais existem nela.
# 	ENTRADA: boa noite                      SAÍDA: 5


frase = input("Digite uma frase: ")
lista_vogais = ["a", "e", "i", "o", "u"]
cont = 0
for letra in frase:
    if letra in lista_vogais:
        cont += 1
print(f"A quantidade de vogais na frase é {cont}")
