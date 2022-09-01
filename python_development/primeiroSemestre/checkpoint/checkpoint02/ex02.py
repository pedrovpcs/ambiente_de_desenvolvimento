# PROGRAMA 2 – até 3,5pts
# Para calcular o INSS respeita-se a tabela:
# SALÁRIO	ALIQUOTA INSS
# Até 1212,00	7,5%
# De 1212,01 até 2427,35	9%
# De 2427,36 até 3641,03	12%
# De 3641,04 até 7087,22	14%
# TETO (Acima de 7087,23)	R$ 992,21
# Fazer um programa que peça o salário e informe em reais o valor de INSS que será pago.
# ENTRADA 1: 3505,76	SAÍDA 1: 420,69
# ENTRADA 2: 9943,71	SAÍDA 2: 992,21


salario = float(input("Digite o valor do salário em reais: "))
if salario <= 1212:
    valor_inss = salario * 0.075
if 1212.01 <= salario <= 2427.35:
    valor_inss = salario * 0.09
if 2527.36 <= salario <= 3641.03:
    valor_inss = salario * 0.12
if 3641.04 <= salario <= 7087.22:
    valor_inss = salario * 0.14
if salario >= 7087.23:
    valor_inss = 992.21
print(f"O valor do INSS é de: R${valor_inss :.2f}")
