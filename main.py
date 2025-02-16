# DESAFIO

# MISSÃO 1 - Restaurando as Regras Escolares
nota_aluno1 = 6
if nota_aluno1 >= 6:
    print("Aprovado")
else:
    print("Reprovado")
# #------------------------------------------

# MISSÃO 2 - O Sistema Eleitoral Secreto
sistema_votação = input("Digite a sua idade: ")
if int(sistema_votação) >= 16:
    print("Você pode votar")
else:
    print("Você ainda não pode votar") 
#-------------------------------------------

# MISSÃO 3 - Recuperando o Sistema de Notas
nota_aluno2 = 60
if nota_aluno2 >= 90 and nota_aluno2 < 101:
    print("Parabéns, você tirou A!")
elif nota_aluno2 >= 80 and nota_aluno2 < 90:
    print("Muito bem, você tirou B.")
elif nota_aluno2 >= 70 and nota_aluno2 < 80:
    print("Bom trabalho, você tirou C.")
elif nota_aluno2 >= 60 and nota_aluno2 < 70:
    print("Fique atento, você tirou D.")
elif nota_aluno2 < 60:
    print("Estude um pouco mais, você tirou F.")
#-----------------------------------------------

# MISSÃO 4 - Restaurando a Identificação de Números
calculo1 = int(input("Escreva o primeiro número: "))
calculo2 = int(input("Escreva o segundo número: "))
soma = calculo1 + calculo2
print(f"A soma dos números é: {soma}")
#--------------------------------------------------

# MISSÃO 5 - Recuperando o Cofre de Segurança
sistema_seguranca = input("Digite a senha: ")
if sistema_seguranca == "Python123":
    print("Acesso liberado")
else:
    print("Acesso negado")
#--------------------------------------------------

# MISSÃO 6 - Reforçando a Segurança e a Contagem do Sistema
numero = 1
while numero < 10:
    numero += 1
    print(numero)
#----------------------------------------------------

# MISSÃO 7 - Organizando a Lista
lista = [8,3,10,1,5]
lista.sort()
print (lista)
#----------------------------------------------------

# MISSÃO 8 - Acessando os Registros de Alunos
tupla = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
print(tupla[0], tupla[-1])
#-------------------------------------------------------

# MISSÃO 9: Calculando Dobro de um Número
numero = 5
def dobro(numero):
	return 2 * numero
print(dobro(numero))
#-----------------------------------------------------

# MISSÃO 10 - Contando Letras
nome = input("Digite um nome: ")
letras = len(nome)
print("A quantidade de letras do nome é:", letras)
#-----------------------------------------------------