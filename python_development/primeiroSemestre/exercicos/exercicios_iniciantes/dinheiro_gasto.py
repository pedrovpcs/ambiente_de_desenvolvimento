#!/bin/env python

# 8. Dado o preço do maço de cigarros, a quantidade de maços consumidos por dia e o
# tempo em anos que a pessoa fuma, calcular o quanto esta pessoa já́ gastou fumando.
# Entrada:	10 1	 3	 Saída:	10950
# Entrada:	11.5	 2 5	 Saída:	41975


cigarette_price = input("Digite o preço do maço de cigarros: ")
cigarette_price = float(cigarette_price)

daily_cigarette_consumed = input("Digite a quantidade de maços consumidos por dia: ")
daily_cigarette_consumed = int(daily_cigarette_consumed)

time_smoking = input("Digite o tempo fumando, em anos: ")
time_smoking = float(time_smoking)

money_spent = cigarette_price * daily_cigarette_consumed * time_smoking * 365
print(f"Esta pessoa já gastou R${money_spent:.2f}")
