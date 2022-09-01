"""
EXERCÍCIOS:
1 - Preencher uma lista com dez elementos float.
2 - Exibir o conteúdo de uma lista
3 - Somar os elementos numéricos da lista
4 - Calcular a média dos elementos
5 - Verificar quantos elementos estão acima da média
6 - mostrar o maior e o menor item da lista. min() e max()
7 - Exibir apenas os elementos negativos
8 - Exibir os elementos com índice ímpar
9 - Verificar se um elemento passado por parâmetro está na lista
10 - Guardar numa segunda lista boleana True caso o elemento esteja acima da média, caso contrário False
"""
############## DEFINIÇÃO DOS SUBALGORITMOS ####################
"""
Preencher uma lista com dez elementos float.
PROTÓTIPO: preencheLista(l: lista): void
"""


def preencheLista(l):  # l é chamado de parâmetro formal
    for i in range(0, 10, 1):
        elemento = float(input(f"{' '*12}Digite o {i + 1}.o elemento: "))
        l.append(elemento)


"""
Exibe uma lista com dez elementos float.
PROTÓTIPO: exibeLista(l: lista): void
"""


def exibeLista(l):
    for i in range(0, 10, 1):
        print(f"{' '*12}Elemento {i+1} = {l[i]}")


"""
Soma os elementos da lista.
PROTÓTIPO: somaElementos(l: lista): Float
"""


def somaElementos(l):
    soma = 0
    for i in range(0, 10, 1):
        soma += l[i]
    return soma


"""
Média dos elementos da lista.
PROTÓTIPO: mediaElementos(l: lista): Float
"""


def mediaElementos(l):
    return somaElementos(l) / 10


"""
Verificar quantos elementos estão acima da média
"""


def elementosAcimaDaMedia(l):
    count = 0
    media = mediaElementos(l)
    for e in l:
        if e > media:
            count += 1
    return count


"""
mostrar o maior e o menor item da lista. min() e max()
"""


def cloneMin(l):
    menor = l[0]
    for x in l:
        if x < menor:
            menor = x
    return menor


def cloneMax(l):
    maior = l[0]
    for x in l:
        if x > maior:
            maior = x
    return maior


def exibeMaiorMenor(l):
    print(f"Menor item da lista: {cloneMin(l)}\n" f"Maior item da lista: {cloneMax(l)}")


"""
Exibir apenas os elementos negativos
"""


def somenteNegativos(l):
    tempList = []
    for x in l:
        if x < 0:
            tempList.append(x)
    return tempList


def exibeSomenteNegativos(l):
    print(somenteNegativos(l))


"""
Exibir os elementos com índice ímpar
"""


def filtroImpar(l):
    tempList = []
    posicao = 0
    for x in l:
        if posicao % 2 != 0:
            tempList.append(x)
        posicao += 1
    return tempList


def exibeSomenteComIndiceImpar(l):
    print(filtroImpar(l))


"""
Verificar se um elemento passado por parâmetro está na lista
"""


def verificaSeExiste(elemento, lista):
    # if elemento in lista ...
    for x in lista:
        if x == elemento:
            return True
    return False


"""
Guardar numa segunda lista boleana True caso o elemento esteja acima da média, caso contrário False
"""


def criarListaBooleana(l):
    tmpList = []
    media = mediaElementos(l)
    for x in l:
        if x > media:
            tmpList.append(True)
        else:
            tmpList.append(False)
    return tmpList


"""
Exibe o menu.
PROTÓTIPO: menu(): void
"""


def menu():
    print(
        """
            ######### M E N U #########
            0  - Sair
            1  - Preencher a Lista
            2  - Exibir a Lista
            3  - Somar os elementos da lista
            4  - Media dos elementos da lista
            5  - Verificar quantos elementos da lista estão acima da média
            6  - Exibir o maior e o menor item da lista
            7  - Exibir apenas os elementos negativos da lista
            8  - Exibir os elementos com índice ímpar
            9  - Verificar se um elemento passado por parâmetro está na lista
            10 - Guardar numa segunda lista boleana True caso o elemento esteja acima da média, caso contrário False
    """
    )


############## PROGRAMA PRINCIPAL ####################
lista = []
listaBooleana = []
while True:
    menu()
    opcao = int(input(f"{' '*12}Digite a opção: "))
    # if opcao == 0:
    #     break
    # elif opcao == 1:
    #     preencheLista(lista) # lista é chamada de parâmetro Real
    # elif opcao == 2:
    #     exibeLista(lista)
    # elif opcao == 3:
    #     print(f"{' '*12}Soma = {somaElementos(lista)}")
    # elif opcao == 4:
    #     print(f"{' ' * 12}Media = {mediaElementos(lista)}")

    match (opcao):
        case 0:
            break
        case 1:
            preencheLista(lista)  # lista é chamada de parâmetro Real
        case 2:
            exibeLista(lista)
        case 3:
            print(f"{' ' * 12}Soma = {somaElementos(lista)}")
        case 4:
            print(f"{' ' * 12}Media = {mediaElementos(lista)}")
        case 5:
            print(f"Elementos acima da media: {elementosAcimaDaMedia(lista)}")
        case 6:
            exibeMaiorMenor(lista)
        case 7:
            exibeSomenteNegativos(lista)
        case 8:
            exibeSomenteComIndiceImpar(lista)
        case 9:
            numero = int(input("Digite o numero que deseja verificar: "))
            if verificaSeExiste(numero, lista) == True:
                print("Existe")
            else:
                print("Nao existe")
        case 10:
            listaBooleana = criarListaBooleana(lista)
            print(listaBooleana)
        case _:
            print("Opcao invalida!")
