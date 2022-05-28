#!/bin/python env

# 5 - Verificar quantos elementos estão acima da média

lista = [2.3, 1.5, 4.6, 7.8, 9.5, 8.2, 0.7, 6.4, 3.2, 0.2]
soma = 0
for i in range(10):
    soma += lista[i]
media = soma / (i + 1)

cont = 0
for i in range(10):
    if (
        lista[i] > media
    ):  # não se esquecer que "lista[i]" analisa elemento por elemento.
        cont += 1


print(f"A  média é de {media} e há {cont} elementos acima dela")
