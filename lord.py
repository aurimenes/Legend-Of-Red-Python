from msvcrt import getche
import random
import time
import os

nivel = 12
pontos = 10 * nivel
dinheiro = 0
monstros = ['detonator', 'pegasus', 'strogonoff']

os.system("")

WHITE = "\033[1;97m"
YELLOW = "\033[1;33m"
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[1;32m"
MAGENTA = "\033[1;35m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

SEPARADOR = "\n  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
SEPARADOR2 = "*****************************************************************"

def mostrar(mensagem):
    print("  " + GREEN + mensagem)
    # time.sleep(1)

def lutar():
    global pontos

    mostrar("\n\n  A luta!" + SEPARADOR)
    sorte = random.randrange(0, len(monstros))
    monstro = monstros[sorte]
    mpontos = random.randrange(5 * nivel, 9 * nivel)

    sorte = random.randrange(0, 5)

    if (sorte == 0):
        mostrar("Você dá de cara com um " + WHITE + monstro + GREEN + "!")
    elif (sorte <= 2):
        mostrar("Um " + WHITE + monstro + GREEN + " aparece bem na sua frente!")
    elif (sorte <= 4):
        mostrar("Você encontrou um " + WHITE + monstro + GREEN + "!")
    elif (sorte == 5):
        mostrar("Cuidado! Tem um " + WHITE + monstro + GREEN + " vindo em sua direção!")

    while True:
        mostrar("Ele tem " + WHITE + str(mpontos) + GREEN  + " pontos")
        mostrar("Você tem " + WHITE + str(pontos) + GREEN  + " pontos")

        mostrar("\n  O que você vai fazer?")
        mostrar("\n  [" + MAGENTA + "A" + GREEN + "]tacar!\n"
            "  [" + MAGENTA + "C" + GREEN + "]orrer com medo")
        
        print(GREEN + "\n  Sua opção: ", end = "")
        acao = getche()

        if (acao == b'a') or (acao == b'A'):
            # Atacando o monstro
            sorte = random.randrange(0 * nivel, 7 * nivel)

            if (sorte == 0):
                mostrar("\n\n  Você tentou atacar o monstro, mas" + WHITE + " ERROU!")
            else:
                mostrar("\n\n  Você atingiu o monstro com " + WHITE + str(sorte) + GREEN + " pontos")
                mpontos = mpontos - sorte

            # Monstro atacando, só se ele não morrer antes
            if (mpontos > 0):
                sorte = random.randrange(0 * nivel, 5 * nivel)

                if (sorte == 0):
                    mostrar("O monstro tentou te atacar, mas" + WHITE + " ERROU!")
                else:
                    mostrar("O monstro lhe atingiu com " + WHITE + str(sorte) + GREEN + " pontos")
                    pontos = pontos - sorte

            mostrar("\n")

            if (mpontos <= 0):
                mostrar(YELLOW + "Você venceu! \o/")

                sorte = random.randrange(1 * nivel, 4 * nivel) # TODO: A pontuacao pode ser variavel, com relação à força original do monstro
                mostrar("Você ganhou " + WHITE + str(sorte) + GREEN + " pontos!")
                pontos = pontos + sorte
                return
            elif (pontos <= 0):
                mostrar(RED + "Você perdeu! :-(")
                mostrar("Tente novamente amanhã")
                exit()

        elif (acao == b'c') or (acao == b'C'):
            mostrar("\n\n  Você dá meia volta e corre!")

            sorte = random.randrange(0, 9)

            if (sorte >= 8):
                mostrar("\n  O " + WHITE + monstro + GREEN + " foi mais rápido que você, e conseguiu lhe atingir!")
                mostrar(WHITE + SEPARADOR2 + "\n")

                sorte = random.randrange(1 * nivel, 3 * nivel)

                mostrar("O ataque do monstro lhe tirou " + str(sorte) + " pontos")
                pontos = pontos - sorte
            else:
                mostrar("O monstro dá risadas ao lhe ver fugindo.")

            return
        else:
            mostrar("\n*** Opção inválida! ***\n")

def forest():
    while True:
        mostrar("\n  A floresta" + SEPARADOR)
        
        mostrar("Você tem " + WHITE + str(pontos) + GREEN + " pontos.")
        mostrar("\n  O que deseja fazer agora?")
        mostrar("\n  [" + MAGENTA + "P" + GREEN + "]rocurar alguma coisa pra matar\n" +
            "  [" + MAGENTA + "V" + GREEN + "]oltar para a cidade")

        print(GREEN + "\n  Sua opção: ", end = "")
        acao = getche()
        mostrar("")
        
        if (acao == b'v') or (acao == b'V'):
            return
        elif (acao == b'p') or (acao == b'P'):
            lutar()
        else:
            mostrar("\n*** Opção inválida! ***\n")

random.seed()

os.system("cls")
mostrar("\n\n  A lenda do dragão vermelho\n\n")
mostrar("A Cidade" + SEPARADOR +
        "\n  As ruas estão lotadas de cidadãos cumprindo seus afazeres\n\n")

forest()