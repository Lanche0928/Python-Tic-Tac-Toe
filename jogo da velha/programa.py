import random

numeros = [1,2,3,4,5,6,7,8,9]
tabuleiro = [[1,2,3],
             [4,5,6],
             [7,8,9]]
colunas = 3
linhas = 3
    
#seleção um jogador ou dois jogadores
def menuJogo():
    selecao = int(input('selecione o número de jogadores:[1] 1 jogador [2] 2 jogadores'))
    if(selecao > 2 or selecao < 1):
        print('Selicione um número válido!')
        return menuJogo()
    
    return selecao


numJogadores = menuJogo()
#nome do Jogador 1
if(numJogadores == 1):
    nome = input('Jogador: ')
#nome dos 2 Jogadores
elif(numJogadores == 2):
    nome = input('Jogador1: ')
    nome2 = input('Jogador2: ')

#desenha o tabuleiro
def printTabuleiro():
    for x in range(linhas):
        print('\n+---+---+---+')
        print('|', end='')
        for y in range(colunas):
            print('', tabuleiro[x][y], end=' |')
    print("\n+---+---+---+")


def mudaTabuleiro(num, turn):
    num -= 1
    if(num == 0):
        tabuleiro[0][0] = turn
    elif(num == 1):
        tabuleiro[0][1] = turn
    elif(num == 2):
        tabuleiro[0][2] = turn
    elif(num == 3):
        tabuleiro[1][0] = turn
    elif(num == 4):
        tabuleiro[1][1] = turn
    elif(num == 5):
        tabuleiro[1][2] = turn
    elif(num == 6):
        tabuleiro[2][0] = turn
    elif(num == 7):
        tabuleiro[2][1] = turn
    elif(num == 8):
        tabuleiro[2][2] = turn

#verifica qual símbolo é o vencedor
def Vencedor(tabuleiro):
    simbolos = ['X', 'O']
    vencedor = 'N'
    for naipe in simbolos:
        #horizontal
        if(tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == naipe  or
        tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] == naipe or
        tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == naipe or   
        #vertical
        tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] == naipe or
        tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] == naipe or
        tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == naipe or
        #cruzado
        tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == naipe or
        tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == naipe):
            print('\n',naipe, ' é o vencedor')    
            vencedor = naipe
            break
        else:
            vencedor = 'N' 
    return vencedor


fimLoop = False
numTurno = 0


def jogadaPlayer(player):
    printTabuleiro()
    escolhaNum = int(input('\nEscolha um número de 1 a 9: '))
    if(escolhaNum >= 1 and escolhaNum <= 9):
        mudaTabuleiro(escolhaNum, player)
        numeros.remove(escolhaNum)
    else:
        print('escolha um número válido')
        jogadaPlayer(player)


while(fimLoop == False):
    #turno Jogador 1
    if(numTurno % 2 == 0):
        jogadaPlayer('X')
        numTurno += 1
    else:
    #turno Jogador 2
        if(numJogadores > 1):
            jogadaPlayer('O')
    #turno PC
        else:
            PCjogada = random.choice(numeros)
            print('\njogada do PC: ', PCjogada)
            if(PCjogada in numeros):
                mudaTabuleiro(PCjogada, 'O')
                numeros.remove(PCjogada)
        numTurno += 1
    vitoria = Vencedor(tabuleiro)
    if(vitoria != 'N'):
        printTabuleiro()
        print('\nJogo finalizado!')
        break





