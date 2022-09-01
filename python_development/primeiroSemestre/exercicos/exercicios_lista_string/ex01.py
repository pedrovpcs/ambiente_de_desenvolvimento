#!/bin/python env

# 1. Dada uma frase pelo usuário, fazer o que cada rotina solicita:
# Exemplo de frase:            ENTRADA: “estou gostando de string no python”
#  Exibir a quantidade de caracteres da frase
# 	SAÍDA: 34

frase = input("Digite uma frase: ")
tamanho = len(frase)                #len irá contar a quantidade de bytes de uma string.
print(tamanho)
