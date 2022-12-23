import random

def jogo():
    print ('----------------------------------------------------------------------')
    print ('                         JOGO DA ADIVINHAÇÃO                          ')
    print ('----------------------------------------------------------------------')

    num_secreto = random.randrange(1, 101)
    total_chutes = 0
    pontos = 1000
    print("Você começa com {} pontos.".format(pontos))
    print("A cada erro será debitado dos pontos, o total da subtração do número secreto com o chute feito.\n")
    print("NÍVEIS DO JOGO")
    print("Nível 1 (fácil)\nNível 2 (médio)\nNível 3 (difícil)\n")

    nivel = int(input("Escolha o nível: "))
    if(nivel == 1): 
        total_chutes = 15
    elif (nivel == 2):
        total_chutes = 10
    elif(nivel == 3):
        total_chutes = 5
    else:
        print("Nível inexistente.")

    for rodada in range(1, total_chutes + 1):
        print("Tentativa {} de {}".format(rodada, total_chutes) )
        
        chute = int(input("Digite um número de 1 a 100: "))
        print('Você digitou', chute)


        if(chute< 1 or chute > 100):
            print("Inserção inválida. Digite um número de 1 a 100:")
            continue
        
        acertou = (chute == num_secreto)
        menor = (chute < num_secreto)
        maior = (chute > num_secreto)
        
        if(acertou):
            print("Parabéns, você acertou e fez {} pontos!!".format(pontos))
            break
        else:
            pontos_perdidos = abs(num_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(menor):
                print("Que pena, você errou... O seu chute foi menor que o número secreto.")
                if (total_chutes == rodada):
                    print("O número secreto era {}. Você fez {} pontos.".format(num_secreto, pontos))
            elif(maior):
                print("Que pena, você errou... O seu chute foi maior que o número secreto.")
                if(total_chutes == rodada):
                    print("O número secreto era {}. Você fez {} pontos.".format(num_secreto, pontos))


    print("FIM DO JOGO")

if(__name__ == "__main__"):
    jogo()