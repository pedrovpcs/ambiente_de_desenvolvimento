#!/bin/env python

# 9. Um caixa eletrônico dispensa cédulas de 50, 20 e 10 reais. Considerando que a
# quantia seja múltiplo de 10, fazer um algoritmo que exiba um relatório com quantas
# cédulas de cada serão necessárias para compor esta quantia.
# Entrada: 130 Saída: 50=2	 20=1	 10=1
# Entrada: 270	 Saída: 50=5	 20=1 10=0

money_amount = input("Digite a quantidade que deseja sacar: ")
money_amount = int(money_amount)


bank_note50 = money_amount // 50
bank_note20 = money_amount % 50 // 20
bank_note10 = money_amount % 50 % 20 // 10

print(
    f"Será necessário {bank_note50} nota(s) de 50, {bank_note20} nota(s) de 20 e {bank_note10} nota(s) de 10"
)
