################ DEFINIÇÃO DOS SUBALGORITMOS #########################
"""
Verifica se uma nota é válida ou não
PROTÓTIPO: notaValida(nota: Float): Boolean
"""
def notaValida(nota):
    return nota >= 0 and nota <= 10

"""
Exibe uma mensagem de nota inválida
PROTÓTIPO: msgNotaInvalida(nota: Float): void
"""
def msgNotaInvalida(nota):
    print(f"A nota {nota} não é válida. \nDigite uma nota entre 0 e 10: ", end = '')

"""
Retorna o menor entre três valores
PROTÓTIPO: menor3n(n1, n2, n3: Float): float
"""
def menor3n(n1, n2, n3):
    menor = n1
    if n2 < menor:
        menor = chk2
    if n3 < menor:
        menor = chk3
    return menor

"""
Calcular a média dos CheckPoints
PROTÓTIPO: mediaCheckpoints(n1, n2, n3: Real): Real
"""
def mediaCheckpoints(n1, n2, n3):
    return (n1 + n2 + n3 - menor3n(n1, n2, n3)) / 2

"""
Calcular a média de 2 valores
PROTÓTIPO: media2n(n1, n2: Real): Real
"""
def media2n(n1, n2):
    return (n1 + n2) / 2

"""
Calcular a porcentagem de um valor
PROTÓTIPO: porcentagemValor(valor, percentual: Real): Real
"""
def porcentagemValor(valor, percentual):
    return valor * percentual

"""
Calcular a soma de 3 numeros
PROTÓTIPO: soma3n(n1, n2, n3: Real): Real
"""
def soma3n(n1, n2, n3):
    return n1 + n2 + n3

"""
Calcular a soma de 2 numeros
PROTÓTIPO: soma2n(n1, n2: Real): Real
"""
def soma2n(n1, n2):
    return n1 + n2

"""
Exibe se está aprovado ou reprovado
PROTÓTIPO: exibeStatus(media: Real): String
"""
def exibeStatusFunc(media):
    if media >= 6:
        return "Aprovado!"
    else:
        return "Não Aprovado!"

"""
Exibe se está aprovado ou reprovado
PROTÓTIPO: exibeStatus(media: Real): void
"""
def exibeStatusProc(media):
    if media >= 6:
        print ("Aprovado!")
    else:
        print ("Não Aprovado!")

################ PROGRAMA PRINCIPAL #########################
print("---------------------- P R I M E I R O   S E M E S T R E")
# Leitura dos checkPoints
chk1 = float(input("Digite o Checkpoint 1:"))
while not notaValida(chk1):
    msgNotaInvalida(chk1)
    chk1 = float(input())

chk2 = float(input("Digite o Checkpoint 2:"))
while not notaValida(chk2):
    msgNotaInvalida(chk2)
    chk2 = float(input())

chk3 = float(input("Digite o Checkpoint 3:"))
while not notaValida(chk3):
    msgNotaInvalida(chk3)
    chk3 = float(input())

# Calcula a media dos checkpoints do primeiro semestre
mediaChk = mediaCheckpoints(chk1, chk2, chk3)
print(f"Média dos CheckPoints: {mediaChk:.1f}")

# Leitura dos Sprints
sprint1 = float(input("Digite o Sprint 1:"))
while not notaValida(sprint1):
    msgNotInvalida(sprint1)
    sprint1 = float(input())

sprint2 = float(input("Digite o Sprint 2:"))
while not notaValida(sprint2):
    msgNotaInvalida(sprint2)
    sprint2 = float(input())

# Calculando a média dos Sprints
mediaSprint = media2n(sprint1, sprint2)
print(f"Média dos Sprints: {mediaSprint:.1f}")

# Lendo a  nota da prova semestral
provaSemestral = float(input("Digite prova semestral:"))

# Ponderando os valores das médias
pontosChk = porcentagemValor(mediaChk, 0.2)
pontosSprints = porcentagemValor(mediaSprint, 0.2)
pontosSemestral = porcentagemValor(provaSemestral, 0.6)

# Cálculo da media do primeiro semestre
mediaPrimeiroSemestre = soma3n(pontosChk, pontosSprints, pontosSemestral)
print(f"Média do 1. Semestre: {mediaPrimeiroSemestre:.2f}")


# Pontos obtidos no primeiro semestre
pontosPrimeiroSemestre = porcentagemValor(mediaPrimeiroSemestre, 0.4)

print (pontosPrimeiroSemestre)

print("---------------------- S E G U N D O   S E M E S T R E")
# Leitura dos checkPoints
chk1 = float(input("Digite o Checkpoint 1:"))
while not notaValida(chk1):
    msgNotaInvalida(chk1)
    chk1 = float(input())

chk2 = float(input("Digite o Checkpoint 2:"))
while not notaValida(chk2):
    msgNotaInvalida(chk2)
    chk2 = float(input())

chk3 = float(input("Digite o Checkpoint 3:"))
while not notaValida(chk3):
    msgNotaInvalida(chk3)
    chk3 = float(input())

# Calcula a media dos checkpoints do primeiro semestre
mediaChk = mediaCheckpoints(chk1, chk2, chk3)
print(f"Média dos CheckPoints: {mediaChk:.1f}")

# Leitura dos Sprints
sprint1 = float(input("Digite o Sprint 1:"))
while not notaValida(sprint1):
    msgNotInvalida(sprint1)
    sprint1 = float(input())

sprint2 = float(input("Digite o Sprint 2:"))
while not notaValida(sprint2):
    msgNotaInvalida(sprint2)
    sprint2 = float(input())

# Calculando a média dos Sprints
mediaSprint = media2n(sprint1, sprint2)
print(f"Média dos Sprints: {mediaSprint:.1f}")

# Lendo a  nota da prova semestral
provaSemestral = float(input("Digite prova semestral:"))

# Ponderando os valores das médias
pontosChk = porcentagemValor(mediaChk, 0.2)
pontosSprints = porcentagemValor(mediaSprint, 0.2)
pontosSemestral = porcentagemValor(provaSemestral, 0.6)

# Cálculo da media do primeiro semestre
mediaSegundoSemestre = soma3n(pontosChk, pontosSprints, pontosSemestral)
print(f"Média do 2. Semestre: {mediaSegundoSemestre:.2f}")


# Pontos obtidos no primeiro semestre
pontosSegundoSemestre = porcentagemValor(mediaSegundoSemestre, 0.6)

print (pontosSegundoSemestre)
# Cálculo da média final
mediaFinal = soma2n(pontosPrimeiroSemestre, pontosSegundoSemestre)

print (f"Média Final: {mediaFinal:.1f} - ", end="")

print (exibeStatusFunc(mediaFinal))
exibeStatusProc(mediaFinal)




"""
# --------------------- S E G U N D O   S E M E S T R E
print("SEGUNDO SEMESTRE")
# Leitura dos checkpoints
chk1 = float(input("Digite o Checkpoint 1:"))
chk2 = float(input("Digite o Checkpoint 2:"))
chk3 = float(input("Digite o Checkpoint 3:"))
# Verificando o Checkpoint de menor valor
menor = chk1
if chk2 < menor:
    menor = chk2
if chk3 < menor:
    menor = chk3
# Calculando a média dos Checkpoints
mediaChk = (chk1 + chk2 + chk3 - menor) / 2
print("Média dos CheckPoints: ", mediaChk)

# Leitura dos Sprints
sprint1 = float(input("Digite o Sprint 1:"))
sprint2 = float(input("Digite o Sprint 2:"))

# Calculando a média dos Sprints
mediaSprint = (sprint1 + sprint2) / 2
print("Média dos Sprints: ", mediaSprint )

# Leitura da prova semestral
semestral = float(input("Digite prova semestral:"))

# Ponderando os valores das médias
pontosChk = mediaChk * 0.2
pontosSprints = mediaSprint * 0.2
pontosSemestral = semestral * 0.6

# Cálculo da media do segundo semestre
mediaSegundoSemestre = (pontosChk + pontosSprints + pontosSemestral)

# Pontos obtidos no segundo semestre
pontosSegundoSemestre = mediaSegundoSemestre * 0.6

# Exibiçao da media do primeiro semetre
print (f"\nMédia do Primeiro Semestre: {mediaPrimeiroSemestre:.1f}")
# Exibiçao da media do segundo semetre
print (f"Média do Segundo Semestre: {mediaSegundoSemestre:.1f}")
# Cálculo da média final
mediaFinal = pontosPrimeiroSemestre + pontosSegundoSemestre
print (f"Média Final: {mediaFinal:.1f} - ", end="")
if mediaFinal >= 6:
    print("Aprovado!")
else:
    print("Não Aprovado!")

"""















