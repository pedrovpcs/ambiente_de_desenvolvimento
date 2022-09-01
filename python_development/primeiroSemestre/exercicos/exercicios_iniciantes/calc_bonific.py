#Aula com o jvcarli (GitHub)


# vendaMensal = input("digite a renda do funcionário: ")
# bonificacao = input("digite a bonificação: ")


def ehNumero(inputDoUsuario, mensagemParaUsuario):
    while not (inputDoUsuario.isnumeric()):
        inputDoUsuario = input(mensagemParaUsuario)
    else:
        inputDoUsuario = float(inputDoUsuario)
    numero = inputDoUsuario
    return numero


# while not (vendaMensal.isnumeric()):
#     vendaMensal = input("digite um numero seu animal: ")

# while not (bonificacao.isnumeric()):
#     bonificacao = input("digite a bonificaçao novamente, caralho: ")

# vendaMensal = float(vendaMensal)
# bonificacao = float(bonificacao)


mensagemDeErro = "Valor incorreto! "
mensagemVenda = "Digite a renda: "
valorVendaMensal = input(mensagemVenda)

valorVendaMensal = ehNumero(valorVendaMensal, mensagemDeErro + mensagemVenda)

mensagemBonificacao = "Digite a bonificacao: "
valorBonificacao = input(mensagemBonificacao)

valorBonificacao = ehNumero(valorBonificacao, mensagemDeErro + mensagemBonificacao)


if valorVendaMensal > 1000:
    if valorBonificacao > 200:
        valorBonificacao = 200
    print(f"{valorVendaMensal:.2f}\n{valorBonificacao}")
else:
    if valorBonificacao > 50:
        valorBonificacao = 50
    print(f"{valorBonificacao:.2f}\n{valorBonificacao}")
