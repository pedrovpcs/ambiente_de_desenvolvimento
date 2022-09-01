#!/bin/env python

# 1. Crie um procedimento chamado "saudacao3" que passe como parâmetro uma MSG: "Bom dia", "Boa Tarde" ou "Boa noite"
# e um NOME e exiba a mensagem na tela:
# protótipo: saudacao3(msg, nome)
# Tela: Boa noite Edson, seja bem vindo a FIAP


def saudacao3(msg, nome):
    print(f"{msg}, {nome} seja bem-vindo à FIAP")


saudacao3("Bom dia", "Pedro")
