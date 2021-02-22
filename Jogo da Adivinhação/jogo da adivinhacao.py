import random

def jogar():


    print("***************************")
    print("Bem vindo ao jogo da adivinhação!")
    print("***************************\n")

    numero_secreto = random.randrange(1,1001)
    total_de_tentativas= 3 
    pontos = 1000

    print("Qual o nível de dificuldade ?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel ==2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas+1):
        
        print("Tentativas {} de {}" .format(rodada, total_de_tentativas))

        chute = int(input("digite um número entre 1 e 1000:")) 

        if(chute<1 or chute> 1000):
            print("Você deve digitar um número entre 1 e 1000")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!!!".format(pontos))
            break

        else:

            if(maior):
                print("Você errou. O seu chute foi maior que o número secreto")

            elif(menor):

                print("Você errou. O seu chute foi menor")
            pontos_perdidos = abs(numero_secreto - chute) 
            pontos = pontos - pontos_perdidos 
        
    print("\nFim de Jogo")


if(__name__ == "__main__"):
    jogar()