#!/bin/env python

# 2. Crie um procedimento chamado "saudacao4" que passe como parâmetro uma HORA e um NOME e exiba a mensagem na tela:
# protótipo: saudacao4(16, nome)
# Tela: <Boa TARDE> <Edson>, seja bem vindo a FIAP


def saudacao4(hora, nome):
    if hora >= 12 and hora <= 18:
        hora = "Boa tarde"
    elif hora > 18:
        hora = "Boa noite"
    else:
        hora = "Bom dia"
    print(f"{hora}, {nome}! Seja bem vindo à FIAP")


saudacao4(12, "Pedro")

# não se esquecer de colocar o parametro entre parenteses quando for uma String
