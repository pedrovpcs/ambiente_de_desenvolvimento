#!/bin/python env

# 9 - Guardar numa segunda lista boleana True caso o elemento esteja acima da média, caso contrário False
# falar sobre a segunda entrega do challenge

soma = 0
acima_media = []
boolean_list = []
lista_elementos = []

for item_lista in range(10):
    elemento = float(input("Digite um número: "))
    lista_elementos.append(elemento)
    boolean_list.append(False)

for elemento in lista_elementos:
    print(elemento)
    soma += elemento
media = soma / 10

for elemento_index in range(0, len(lista_elementos)):
    if lista_elementos[elemento_index] > media:
        acima_media.append(lista_elementos[elemento_index])
        boolean_list.insert(elemento_index, True)
        del boolean_list[elemento_index + 1]

print(
    f"O maior número da lista é {max(lista_elementos)} o menor é {min(lista_elementos)}"
)

print("Os números negativos são: ")
for elemento in lista_elementos:
    if elemento < 0:
        print(elemento, end=" ")

print("Os elementos de indice impares são: ")
for index_elemento in range(0, len(lista_elementos), 2):
    print(f"{lista_elementos[index_elemento]}", end=" ")

print(boolean_list)
