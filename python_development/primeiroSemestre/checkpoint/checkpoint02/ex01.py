# Na feira, as bananas custam R$ 0,30 cada se forem compradas até uma dúzia e R$ 0,25 cada se a quantidade for superior a uma dúzia.
# Fazer um programa que peça ao usuário a quantidade de bananas desejadas e informe no final o recibo com o preço final e a quantidade de bananas adquiridas
# ENTRADA 1: 15   	SAÍDA 1: 3.75	15
# ENTRADA 2: 10   	SAÍDA 2: 3.00	10


bananas = float(input("Digite a quantidade de bananas desejada: "))
if bananas <= 12:
    valor: float
    valor = 0.3 * bananas
else:
    valor = bananas * 0.25
print(f" Valor a ser pago: R${valor:} e {bananas} bananas.")
