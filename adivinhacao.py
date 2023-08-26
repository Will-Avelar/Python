print("*********************")
print("Jogo da Adivinhação")
print("*********************")

'''
# 1º Versão
numero_secreto = 42
chute = input("Adivinhe o número secreto: ")
print("Você digitou: ", chute)
chute = int(chute)
if(numero_secreto == chute):
    print("Parabéns, você acertou!")
else:
    print("Você Errou!")
if(numero_secreto == chute):
    print('Você Acertou!')
elif(chute < numero_secreto):
    print("O Numero secreto é maior")
elif(chute > numero_secreto):
    print("O número secreto é menor")
'''
    #Extraindo Condições para variáveis
'''
numero_secreto = 42
chute = input("Adivinhe o número secreto: ")
print("Você digitou: ", chute)
chute = int(chute)
acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto
if(acertou):
        print("Você Acertou")
elif(maior):
        print("Seu chute foi maior que o numero secreto")
elif(menor):
        print("Seu chute foi menor que o numero secreto")
'''

#While

