import random

def jogo():
    print ('----------------------------------------------------------------------')
    print ('                            JOGO DA FORCA                             ')
    print ('----------------------------------------------------------------------')

    arquivo = open("palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    espaco_letras = ["_" for letra in palavra_secreta]

    cont = espaco_letras.count("_")
    print("Você tem {} chances.".format(cont))
    print(espaco_letras)

    enforcou = False
    acertou = False
    erros = 0

    while (not acertou and not enforcou):
        chute = input("Qual letra você quer?  ").upper()
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            print("Achamos a letra {} na palavra.".format(chute))
            posicao = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    espaco_letras[posicao] = letra
                posicao += 1
        else:
            erros += 1
            print("Não achamos a letra {} na palavra.".format(chute))
            desenha_forca(erros)

        enforcou = (erros == 7)
        acertou = "_" not in espaco_letras
        print(espaco_letras)

    if(acertou):
        print("Parabéns você ganhou o jogo da forca!!! Achou a palavra secreta: {}.".format(palavra_secreta))
    else:
        print("Que pena, você não achou a palavra secreta :(")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogo()