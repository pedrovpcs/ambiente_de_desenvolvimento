#!/bin/python env

# 3. Em uma votação, existem 3 candidatos: 1 – Huguinho, 2 – Zezinho e 3 – Luizinho.
# Pedir e acumular votos até que em votos seja digitado o numero 0 (zero).
# Ao final, exibir a quantidade de votos de cada usuário.

# 1 – HUGUINHO
# 2 – ZEZINHO
# 3 – LUIZINHO
# 0 - SAIR

# ENTRADA:
# 3 3 2 3 1 3 1 0

# SAÍDA:
# 1 – HUGUINHO: 	2 VOTOS
# 2 – ZEZINHO:	1 VOTO
# 3 – LUIZINHO:	4 VOTOS

voto_huguinho = 0
voto_zezinho = 0
voto_luizinho = 0

voto = int(input("Digite o número do candidato: "))
if voto == 0:  # isso vai finalizar o laço
    print(
        f" HUGUINHO - {voto_huguinho} votos.\n ZEZINHO - {voto_zezinho} votos.\n LUIZINHO - {voto_luizinho} votos. "
    )
else:
    while voto != 0:
        if voto == 1:
            voto_huguinho += 1  # voto_huguinho = voto_huguinho + 1
        elif voto == 2:
            voto_zezinho += 1
        else:  # aqui já mostra para o programa q caso nenhuma das outras condições antecedentes aconteçam, isso será executado.
            voto_luizinho += 1
        voto = int(input("Digite o número do candidato: ")) 
print(
    f" HUGUINHO - {voto_huguinho} votos.\n ZEZINHO - {voto_zezinho} votos.\n LUIZINHO - {voto_luizinho} votos. "
)
