#!/bin/env python

# 9. Crie uma função que passe um número por parâmetro e retorne o seu fatorial.
# Protótipo: fatorial(4)
# Retorno: 24


def fatorial(f):
    resultado = 1
    for n in range(1, f + 1):
        resultado *= n
    return resultado


"""
for n in range(1, f + 1)
1 = onde começa 
f onde termina
o +1, é pq a contagem se inicia no 0, sendo assim... 0,1,2,3,4!
por padrao, se não houver o terceiro numero, a casa se moverá de 1 em 1

"""


z = fatorial(4)
print(z)
