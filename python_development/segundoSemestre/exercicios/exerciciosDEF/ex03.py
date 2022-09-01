#!/bin/env python

# 3. Crie um procedimento chamado "saudacao5" que passe como parâmetro uma HORA e um NOME deixando como padrão
# "Boa Noite" e "Edson" e exiba a mensagem na tela:
# protótipo 1: saudacao5(11, "Maria")
# Bom dia Maria, seja bem vindo a FIAP
# protótipo 2: saudacao5()
# Tela: Boa noite Edson, seja bem vindo a FIAP


def saudacao5(hora=19, nome="Edson"):
    if hora >= 12 and hora <= 18:
        hora = "Boa tarde"
    elif hora > 18:
        hora = "Boa noite"
    else:
        hora = "Bom dia"
    print(f"{hora}, {nome} seja bem vindo(a) á FIAP. ")


saudacao5()

saudacao5(11, "Maria")
