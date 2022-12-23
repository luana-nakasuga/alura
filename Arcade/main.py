import adivinhacao
import forca

def escolher_jogo():
    print ('----------------------------------------------------------------------')
    print ('                         BEM VINDO AO ARCADE!                         ')
    print ('----------------------------------------------------------------------')
    print("\nJOGOS DISPONÍVEIS\n(1) FORCA\n(2) ADIVINHAÇÃO")

    jogo = int(input("Qual jogo você deseja? "))

    if(jogo == 1):
        print("Jogando Forca.")
        forca.jogo()
    elif(jogo == 2):
        print("Jogando Adivinhação.")
        adivinhacao.jogo()
    else:
        print("Jogo inexistente.")

if(__name__ == "__main__"):
    escolher_jogo()    