#!/bin/python env
# EXERCÍCIO

# 1. DADA A VENDA MENSAL DE UM VENDEDOR, DEFINA A SUA BONIFICAÇÃO.

# - SE A VENDA FOR MAIOR DO QUE 1000, ELE GANHARÁ UMA BONIFICAÇÃO DE 100 REAIS

# - SE A VENDA FOR MENOR OU IGUAL A MIL A BONIFICAÇÃO SERÁ DE 10 REAIS

# AO FINAL EXIBIR A VENDA E A BONIFICAÇÃO

# ENTRADA: 5000 SAÍDA: 5000 100

# ENTRADA: 990 SAÍDA: 990 + 10

# bonifiacao_100 = 100
# bonificacao_10 = 10

# if venda_mensal > 1000:
#     venda_mensal = venda_mensal + bonifiacao_100
#     print(f"Bonificação de {bonifiacao_100} reais atingida! {venda_mensal}")

# else: venda_mensal <= 1000
# venda_mensal = (venda_mensal + 10) - 100
# print(f"Bonificação de {bonificacao_10} reais atingida! {venda_mensal}")

# o método de resolução acima está errada. Tem uma maneira mais simples!

# if vendaMensal > 1000:
#     bonificacao = 100
#     print(f"{vendaMensal:.2f}\n100")
# else:
#     bonificacao = 10
#     print(f"{vendaMensal:.2f}\n10")

# Outra forma de resolver, porém, NÃO FAÇA, isso é harcode (embutir dados diretamente no código, nesse caso, foi dentro da string).

venda_mensal = input("Digite o valor de venda mensal: ")
venda_mensal = float(venda_mensal)

if venda_mensal > 1000:
    bonificacao = 100
    venda_mensal = venda_mensal + bonificacao
    print(f"Bonificação de {bonificacao} reais atingida! {venda_mensal}")

else:
    bonificacao = 10
    venda_mensal = venda_mensal + bonificacao
    print(f"Bonificação de {bonificacao} reais atingida! {venda_mensal}")


# 2. Dado o SALÁRIO FIXO do vendedor e a VENDA MENSAL, calcular o comissão do mesmo.

# A comissão é calculada a partir da venda mensal.

# - Se ele vender mais do que 50000, ganhará 7,5% de comissão

# - Se ele vender menos ou igual a 50000 ele ganhará 5% de comissão.

# Ao final exibir o SALARIO FIXO, A VENDA, O VALOR DA COMISSÃO E O SALARIO COM A VENDA
