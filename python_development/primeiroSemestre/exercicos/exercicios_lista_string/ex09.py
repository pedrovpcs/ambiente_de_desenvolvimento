#!/bin/python env

# 9. Dada uma frase, exibí-la de trás pra frente
# 	ENTRADA: estou gostando de string no python
# 	SAÍDA: 	  nohtyp on gnirts ed odnatsog uotse

frase = input("Digite uma frase:").strip()
for index in range(-1, len(frase) * -1 - 1, -1):
    print(frase[index], end="")
