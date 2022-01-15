import random
import os

opcoes = ["pedra", "papel", "tesoura"]
placar_jogador = 0
placar_computador = 0

print("====================")
print("Bem vindo ao jogo de Pedra, Papel e Tesoura")

def print_um():
    print("====================")
    print("Placar:")
    print("Você: {}".format(placar_jogador))
    print("Computador: {}".format(placar_computador))
    print("Escolha uma opção: 0 = pedra; 1 = papel; 2 = tesoura")

def opcao_do_computador():
    return random.choice(opcoes)

def opcao_do_jogador():
    while True:
        try:
            jogador = int(input())
            if jogador not in [0, 1, 2]:
                raise
            return opcoes[jogador]

        except Exception as e:
            print(e)
        
def jogadas(player, computer):
    global placar_jogador, placar_computador

    if player == "pedra":
        if computer == "tesoura":
            placar_jogador += 1
            return "g"
        elif computer == "papel":
            placar_computador += 1
            return "p"
        else:
            return "e"
    if player == "papel":
        if computer == "pedra":
            placar_jogador += 1
            return "g"
        elif computer == "tesoura":
            placar_computador += 1
            return "p"
        else:
            return "d"
    if player == "tesoura":
        if computer == "papel":
            placar_jogador += 1
            return "g"
        elif computer == "pedra":
            placar_computador += 1
            return "p"
        else:
            return "e"

again = 1
while again == 1:
    print_um()
    jogador = opcao_do_jogador()
    computador = opcao_do_computador()
    placar = jogadas (jogador, computador)

    print("")
    print("====================")
    print("Sua Jogada: {}".format(jogador.upper()))
    print("Jogada do Computador: {}".format(computador.upper()))

    if placar == "g":
        print("Você Ganhou!")
    elif placar == "p":
        print("Não foi dessa vez!")
    else:
        print("Empate!")
    print("====================")

    while True:
        print("Continuar jogando? SIM = 0 | NÃO = 1")
        continuar = int(input())
        if continuar == 0:
            break
        elif continuar == 1:
            again = 0
            break

os.system("cls")