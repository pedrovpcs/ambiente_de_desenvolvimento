# Faça um programa que peça para o usuário digitar 15 números e contar quantos números Positivos, Negativos e Nulos foram digitados. Ao final, exibir as quantidades de cada.
# ENTRADA:
# 15 9 -4 3 -7 11 0 0 4 5 8 2 13 41 -15
# SAÍDA:
# Positivos: 10
# Negativos: 3
# Nulos: 2


positivos = 0
negativos = 0
nulos = 0

numero = int(input("Digite um número positivo, negativo ou nulo: "))
volta = 1
while volta <= 15:
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        nulos += 1
    volta += 1
    numero = int(input("Digite um número positivo, negativo ou nulo: "))
print(f" Positivos - {positivos}\n Negativos - {negativos}\n Nulos - {nulos} ")
