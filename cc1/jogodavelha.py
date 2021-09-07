import random
from os import system, name 

def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "2020204959" 

def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "Guilherme Cosme Petri Dalmaso" 

def limpaTela(): 
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear') 

def simboloJogador():
    """
    Função para o jogador escolher X ou O para jogar,
    também define o símbolo do PC de acordo com o que o jogador escolher.
    """
    escolha = input("Escolha X ou O para começar a partida: ")
    if escolha == "x" or escolha == "X":
        simboloPlayer = "X"
        simboloPC = "O"
        return simboloPlayer, simboloPC
    elif escolha == "o" or escolha == "O":
        simboloPlayer = "O"
        simboloPC = "X"
        return simboloPlayer, simboloPC
    else:
        print("Símbolo não reconhecido! Você pode escolher X ou O")
        return simboloJogador()

def jogaPrimeiro(Lista = ["PC","JOGADOR"]):
    """
    Função que escolhe "aleatóriamente" quem começa jogando
    """
    comeca = (random.choice(Lista))
    if comeca == "PC":
        print("O PC joga primeiro")
        return comeca
    elif comeca == "JOGADOR":
        print("Você começa jogando")
        return comeca

def printTabuleiro(tabuleiro):
    """
    Função que imprime o tabuleiro
    """
    print(f" {tabuleiro[7]} | {tabuleiro[8]} | {tabuleiro[9]}")
    print("---+---+---")
    print(f" {tabuleiro[4]} | {tabuleiro[5]} | {tabuleiro[6]}")
    print("---+---+---")
    print(f" {tabuleiro[1]} | {tabuleiro[2]} | {tabuleiro[3]}")

def jogadaPlayer(tabuleiro, simboloPlayer):
    """
    Solicita o jogador para escolher uma posição no tabuleiro
    """
    escolhaJogador = int(input("Escolha uma posição de 1 a 9 no tabuleiro: "))
    if escolhaJogador < 1 or escolhaJogador > 9:
        print("Posição Inválida! Escolha novamente")
        return jogadaPlayer(tabuleiro, simboloPlayer)
    else:
        if tabuleiro[escolhaJogador] != " ":
            print("A posição já foi escolhida! Por favor escolha outra opção")
            return jogadaPlayer(tabuleiro, simboloPlayer)
        else:
            tabuleiro[escolhaJogador] = simboloPlayer
            printTabuleiro(tabuleiro)



def jogadaComputador(tabuleiro, simboloComputador):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas, 
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    simboloComputador: letra do computador
    simboloPlayer: letra do jogador
    i: se for 1, significa que o computador é o primeiro a jogar, caso o contrário, é o segundo

    Retorno:
    Posição (entre 1 e 9) da jogada do computador

    Estratégia:
    Se o Computador for o primeiro a jogar, ele vai escolher alguma das posições das quinas
    Caso o contrário, ele vai verificar se é necessário fazer a defesa
    A partir da 5 rodada, ele vai verificar se já é possível ganhar a partida
    Se não for necessário a defesa, o PC irá atacar
    """

    if simboloComputador == "X":
        simboloPlayer = "O"
    else:
        simboloPlayer = "X"

    if tabuleiro == [" "," "," "," "," "," "," "," "," "," "]:
        escolhaPC = random.choice([1,3,7,9])
        if escolhaPC == 1:
            return 1
        elif escolhaPC == 3:
            return 3
        elif escolhaPC == 7:
            return 7
        elif escolhaPC == 9:
            return 9
    else:
        #ataque linha 1
        if tabuleiro[1] == simboloComputador and tabuleiro[2] == simboloComputador and tabuleiro[3] == " ":
            return 3
        elif tabuleiro[1] == simboloComputador and tabuleiro[3] == simboloComputador and tabuleiro[2] == " ":
            return 2
        elif tabuleiro[2] == simboloComputador and tabuleiro[3] == simboloComputador and tabuleiro[1] == " ":
            return 1           
        #ataque linha 2  
        elif tabuleiro[4] == simboloComputador and tabuleiro[5] == simboloComputador and tabuleiro[6] == " ":
            return 6
        elif tabuleiro[4] == simboloComputador and tabuleiro[6] == simboloComputador and tabuleiro[5] == " ":
            return 5
        elif tabuleiro[5] == simboloComputador and tabuleiro[6] == simboloComputador and tabuleiro[4] == " ":
            return 4   
        #ataque linha 3
        elif tabuleiro[7] == simboloComputador and tabuleiro[8] == simboloComputador and tabuleiro[9] == " ":
            return 9
        elif tabuleiro[7] == simboloComputador and tabuleiro[9] == simboloComputador and tabuleiro[8] == " ":
            return 8
        elif tabuleiro[8] == simboloComputador and tabuleiro[9] == simboloComputador and tabuleiro[7] == " ":
            return 7
        #ataque coluna 1
        elif tabuleiro[1] == simboloComputador and tabuleiro[4] == simboloComputador and tabuleiro[7] == " ":
            return 7
        elif tabuleiro[1] == simboloComputador and tabuleiro[7] == simboloComputador and tabuleiro[4] == " ":
            return 4
        elif tabuleiro[4] == simboloComputador and tabuleiro[7] == simboloComputador and tabuleiro[1] == " ":
            return 1
        #ataque coluna 2
        elif tabuleiro[2] == simboloComputador and tabuleiro[5] == simboloComputador and tabuleiro[8] == " ":
            return 8
        elif tabuleiro[2] == simboloComputador and tabuleiro[8] == simboloComputador and tabuleiro[5] == " ":
            return 5
        elif tabuleiro[5] == simboloComputador and tabuleiro[8] == simboloComputador and tabuleiro[2] == " ":
            return 2    
        #ataque coluna 3
        elif tabuleiro[3] == simboloComputador and tabuleiro[6] == simboloComputador and tabuleiro[9] == " ":
            return 9
        elif tabuleiro[3] == simboloComputador and tabuleiro[9] == simboloComputador and tabuleiro[6] == " ":
            return 6
        elif tabuleiro[6] == simboloComputador and tabuleiro[9] == simboloComputador and tabuleiro[3] == " ":
            return 3 
        #ataque diagonal 1
        elif tabuleiro[1] == simboloComputador and tabuleiro[5] == simboloComputador and tabuleiro[9] == " ":
            return 9
        elif tabuleiro[1] == simboloComputador and tabuleiro[9] == simboloComputador and tabuleiro[5] == " ":
            return 5
        elif tabuleiro[5] == simboloComputador and tabuleiro[9] == simboloComputador and tabuleiro[1] == " ":
            return 1   
        #ataque diagonal 2
        elif tabuleiro[3] == simboloComputador and tabuleiro[5] == simboloComputador and tabuleiro[7] == " ":
            return 7
        elif tabuleiro[3] == simboloComputador and tabuleiro[7] == simboloComputador and tabuleiro[5] == " ":
            return 5
        elif tabuleiro[5] == simboloComputador and tabuleiro[7] == simboloComputador and tabuleiro[3] == " ":
            return 3       

        #defesa linha 1
        elif tabuleiro[1] == simboloPlayer and tabuleiro[2] == simboloPlayer and tabuleiro[3] == " ":
            return 3
        elif tabuleiro[1] == simboloPlayer and tabuleiro[3] == simboloPlayer and tabuleiro[2] == " ":
            return 2
        elif tabuleiro[2] == simboloPlayer and tabuleiro[3] == simboloPlayer and tabuleiro[1] == " ":
            return 1        
        #defesa linha 2
        elif tabuleiro[4] == simboloPlayer and tabuleiro[5] == simboloPlayer and tabuleiro[6] == " ":
            return 6
        elif tabuleiro[4] == simboloPlayer and tabuleiro[6] == simboloPlayer and tabuleiro[5] == " ":
            return 5
        elif tabuleiro[5] == simboloPlayer and tabuleiro[6] == simboloPlayer and tabuleiro[4] == " ":
            return 4
        #defesa linha 3
        elif tabuleiro[7] == simboloPlayer and tabuleiro[8] == simboloPlayer and tabuleiro[9] == " ":
            return 9
        elif tabuleiro[7] == simboloPlayer and tabuleiro[9] == simboloPlayer and tabuleiro[8] == " ":
            return 8
        elif tabuleiro[8] == simboloPlayer and tabuleiro[9] == simboloPlayer and tabuleiro[7] == " ":
            return 7
        #defesa coluna 1
        elif tabuleiro[1] == simboloPlayer and tabuleiro[4] == simboloPlayer and tabuleiro[7] == " ":
            return 7
        elif tabuleiro[1] == simboloPlayer and tabuleiro[7] == simboloPlayer and tabuleiro[4] == " ":
            return 4
        elif tabuleiro[4] == simboloPlayer and tabuleiro[7] == simboloPlayer and tabuleiro[1] == " ":
            return 1
        #defesa coluna 2
        elif tabuleiro[2] == simboloPlayer and tabuleiro[5] == simboloPlayer and tabuleiro[8] == " ":
            return 8
        elif tabuleiro[2] == simboloPlayer and tabuleiro[8] == simboloPlayer and tabuleiro[5] == " ":
            return 5
        elif tabuleiro[5] == simboloPlayer and tabuleiro[8] == simboloPlayer and tabuleiro[2] == " ":
            return 2
        #defesa coluna 3
        elif tabuleiro[3] == simboloPlayer and tabuleiro[6] == simboloPlayer and tabuleiro[9] == " ":
            return 9
        elif tabuleiro[3] == simboloPlayer and tabuleiro[9] == simboloPlayer and tabuleiro[6] == " ":
            return 6
        elif tabuleiro[6] == simboloPlayer and tabuleiro[9] == simboloPlayer and tabuleiro[3] == " ":
            return 3        
        #defesa diagonal 1
        elif tabuleiro[1] == simboloPlayer and tabuleiro[5] == simboloPlayer and tabuleiro[9] == " ":
            return 9
        elif tabuleiro[1] == simboloPlayer and tabuleiro[9] == simboloPlayer and tabuleiro[5] == " ":
            return 5
        elif tabuleiro[5] == simboloPlayer and tabuleiro[9] == simboloPlayer and tabuleiro[1] == " ":
            return 1   
        #defesa diagonal 2
        elif tabuleiro[3] == simboloPlayer and tabuleiro[5] == simboloPlayer and tabuleiro[7] == " ":
            return 7
        elif tabuleiro[3] == simboloPlayer and tabuleiro[7] == simboloPlayer and tabuleiro[5] == " ":
            return 5
        elif tabuleiro[5] == simboloPlayer and tabuleiro[7] == simboloPlayer and tabuleiro[3] == " ":
            return 3    
        #defesa de ataque pelas quinas   
        elif (tabuleiro[1] == simboloPlayer and tabuleiro[9] == simboloPlayer) or (tabuleiro[3] == simboloPlayer and tabuleiro[7] == simboloPlayer):
            if tabuleiro[2] == " ":
                return 2
            elif tabuleiro[4] == " ":
                return 4  
            elif tabuleiro[6] == " ":
                return 6
            elif tabuleiro[8] == " ":
                return 8  
        elif tabuleiro[6] == simboloPlayer and tabuleiro[7] == simboloPlayer and tabuleiro[9] == " ":
            return 9
        #defesa por posições de numero par
        elif tabuleiro[2] == simboloPlayer or tabuleiro[4] == simboloPlayer or tabuleiro[6] == simboloPlayer or tabuleiro[8] == simboloPlayer:
            if tabuleiro[5] == " ":
                return 5    
            elif tabuleiro[1] == " ":
                return 1
            elif tabuleiro[3] == " ":
                return 3
            elif tabuleiro[7] == " ":
                return 7
            elif tabuleiro[9] == " ":
                return 9  
        #defesa por posições de numero ímpar
        elif tabuleiro[1] == simboloPlayer or tabuleiro[3] == simboloPlayer or tabuleiro[7] == simboloPlayer or tabuleiro[9] == simboloPlayer:
            if tabuleiro[5] == " ":
                return 5    
            elif tabuleiro[1] == " ":
                return 1
            elif tabuleiro[3] == " ":
                return 3
            elif tabuleiro[7] == " ":
                return 7
            elif tabuleiro[9] == " ":
                return 9                                        
        #ataque
        elif tabuleiro[1] == " ":
            return 1
        elif tabuleiro[3] == " ":
            return 3
        elif tabuleiro[7] == " ":
            return 7
        elif tabuleiro[9] == " ":
            return 9   
        elif tabuleiro[2] == " ":
            return 2             
        elif tabuleiro[4] == " ":
            return 4
        elif tabuleiro[6] == " ":
            return 6
        elif tabuleiro[8] == " ":
            return 8

def jogadaPC(tabuleiro, simboloComputador, i):
    """
    Atribui a jogada feita pelo computador na função 'jogadaComputador' ao tabuleiro
    """
    if i == 1:
        escolhaPC = jogadaComputador(tabuleiro, simboloComputador)
        if escolhaPC == 1:
            tabuleiro[1] = simboloComputador
            printTabuleiro(tabuleiro)
        elif escolhaPC == 3:
            tabuleiro[3] = simboloComputador
            printTabuleiro(tabuleiro)
        elif escolhaPC == 7:
            tabuleiro[7] = simboloComputador
            printTabuleiro(tabuleiro)
        elif escolhaPC == 9:
            tabuleiro[9] = simboloComputador
            printTabuleiro(tabuleiro)
    else:
        escolhaPC = jogadaComputador(tabuleiro, simboloComputador)
        if escolhaPC == 1:
            tabuleiro[1] = simboloComputador
            printTabuleiro(tabuleiro)
        elif escolhaPC == 2:
            tabuleiro[2] = simboloComputador
            printTabuleiro(tabuleiro)            
        elif escolhaPC == 3:
            tabuleiro[3] = simboloComputador
            printTabuleiro(tabuleiro)
        elif escolhaPC == 4:
            tabuleiro[4] = simboloComputador
            printTabuleiro(tabuleiro)
        elif escolhaPC == 5:
            tabuleiro[5] = simboloComputador
            printTabuleiro(tabuleiro)  
        elif escolhaPC == 6:
            tabuleiro[6] = simboloComputador
            printTabuleiro(tabuleiro)                                      
        elif escolhaPC == 7:
            tabuleiro[7] = simboloComputador
            printTabuleiro(tabuleiro)
        elif escolhaPC == 8:
            tabuleiro[8] = simboloComputador
            printTabuleiro(tabuleiro)            
        elif escolhaPC == 9:
            tabuleiro[9] = simboloComputador
            printTabuleiro(tabuleiro)        

def verificaJogada(tabuleiro):
    """
    Verifica se o 'X' ou 'O' ganhou o Jogo, se até a ultima rodada nenhum dos 2 ganhar, é considerado empate
    """
    #Se X vencer
    #linhas
    if tabuleiro[7] == 'X' and tabuleiro[8] == 'X' and tabuleiro[9] == 'X':
        return True
    elif tabuleiro[4] == 'X' and tabuleiro[5] == 'X' and tabuleiro[6] == 'X':
        return True
    elif tabuleiro[1] == 'X' and tabuleiro[2] == 'X' and tabuleiro[3] == 'X':
        return True
    #colunas
    elif tabuleiro[1] == 'X' and tabuleiro[4] == 'X' and tabuleiro[7] == 'X':
        return True
    elif tabuleiro[2] == 'X' and tabuleiro[5] == 'X' and tabuleiro[8] == 'X':
        return True
    elif tabuleiro[3] == 'X' and tabuleiro[6] == 'X' and tabuleiro[9] == 'X':
        return True
    #diagonal
    elif tabuleiro[1] == 'X' and tabuleiro[5] == 'X' and tabuleiro[9] == 'X':
        return True
    elif tabuleiro[3] == 'X' and tabuleiro[5] == 'X' and tabuleiro[7] == 'X':
        return True    

    #Se O vencer
    #linhas
    if tabuleiro[7] == 'O' and tabuleiro[8] == 'O' and tabuleiro[9] == 'O':
        return True
    elif tabuleiro[4] == 'O' and tabuleiro[5] == 'O' and tabuleiro[6] == 'O':
        return True
    elif tabuleiro[1] == 'O' and tabuleiro[2] == 'O' and tabuleiro[3] == 'O':
        return True
    #colunas
    elif tabuleiro[1] == 'O' and tabuleiro[4] == 'O' and tabuleiro[7] == 'O':
        return True
    elif tabuleiro[2] == 'O' and tabuleiro[5] == 'O' and tabuleiro[8] == 'O':
        return True
    elif tabuleiro[3] == 'O' and tabuleiro[6] == 'O' and tabuleiro[9] == 'O':
        return True
    #diagonal
    elif tabuleiro[1] == 'O' and tabuleiro[5] == 'O' and tabuleiro[9] == 'O':
        return True
    elif tabuleiro[3] == 'O' and tabuleiro[5] == 'O' and tabuleiro[7] == 'O':
        return True    

def main():
    """
    Chama as funções principais e dedtermina a ordem das jogadas
    """
    limpaTela()
    print(getMatricula())
    print(getNome())
    print("SEJA BEM VINDO AO DESAFIO DO JOGO DA VELHA!")
    simboloPlayer, simboloComputador = simboloJogador()
    primeiraJogada = jogaPrimeiro()
    tabuleiro = [" "]*10
    printTabuleiro(tabuleiro)
    if primeiraJogada == "PC":
        #1
        print("VEZ DO PC")
        jogadaPC(tabuleiro, simboloComputador, 1)
        #2
        print("SUA VEZ")
        jogadaPlayer(tabuleiro, simboloPlayer)
        #3
        print("VEZ DO PC")
        jogadaPC(tabuleiro, simboloComputador, 2) 
        #4 
        print("SUA VEZ")
        jogadaPlayer(tabuleiro, simboloPlayer)
        #5
        print("VEZ DO PC")
        jogadaPC(tabuleiro, simboloComputador, 2)    
        verificaJogada(tabuleiro)
        if verificaJogada(tabuleiro) == True:
            print("O Computador venceu a partida!")
            _ = input("Pressione enter para finalizar...")
            exit()
        #6
        print("SUA VEZ")
        jogadaPlayer(tabuleiro, simboloPlayer) 
        verificaJogada(tabuleiro)        
        if verificaJogada(tabuleiro) == True:
            print("Você venceu a partida!")
            _ = input("Pressione enter para finalizar...")
            exit()          
        #7
        print("VEZ DO PC")
        jogadaPC(tabuleiro, simboloComputador, 2)
        verificaJogada(tabuleiro)         
        if verificaJogada(tabuleiro) == True:
            print("O Computador venceu a partida!")
            _ = input("Pressione enter para finalizar...")
            exit()        
        #8
        print("SUA VEZ")
        jogadaPlayer(tabuleiro, simboloPlayer) 
        verificaJogada(tabuleiro)        
        if verificaJogada(tabuleiro) == True:
            print("Você venceu a partida!")
            _ = input("Pressione enter para finalizar...")
            exit()         
        #9
        print("VEZ DO PC")
        jogadaPC(tabuleiro, simboloComputador, 2) 
        verificaJogada(tabuleiro)        
        if verificaJogada(tabuleiro) == True:
            print("O Computador venceu a partida!")
            _ = input("Pressione enter para finalizar...")
            exit()                                                  
        else:
            print("Empate!!!")
            _ = input("Pressione enter para finalizar...")
            exit()
    elif primeiraJogada == "JOGADOR":
        #1
        print("SUA VEZ")
        jogadaPlayer(tabuleiro, simboloPlayer)
        #2
        print("VEZ DO PC")
        jogadaPC(tabuleiro, simboloComputador, 2) 
        #3
        print("SUA VEZ")
        jogadaPlayer(tabuleiro, simboloPlayer)
        #4
        print("VEZ DO PC")
        jogadaPC(tabuleiro, simboloComputador, 2) 
        #5
        print("SUA VEZ")
        jogadaPlayer(tabuleiro, simboloPlayer)
        verificaJogada(tabuleiro)         
        if verificaJogada(tabuleiro) == True:
            print("Você venceu a partida!")
            _ = input("Pressione enter para finalizar...")
            exit()                
        #6
        print("VEZ DO PC")
        jogadaPC(tabuleiro, simboloComputador, 2)
        verificaJogada(tabuleiro) 
        if verificaJogada(tabuleiro) == True:
            print("O Computador venceu a partida!")
            _ = input("Pressione enter para finalizar...")
            exit()                
        #7
        print("SUA VEZ")
        jogadaPlayer(tabuleiro, simboloPlayer) 
        verificaJogada(tabuleiro)        
        if verificaJogada(tabuleiro) == True:
            print("Você venceu a partida!")
            _ = input("Pressione enter para finalizar...")
            exit()                 
        #8
        print("VEZ DO PC")
        jogadaPC(tabuleiro, simboloComputador, 2) 
        verificaJogada(tabuleiro)        
        if verificaJogada(tabuleiro) == True:
            print("O Computador venceu a partida!")
            _ = input("Pressione enter para finalizar...")
            exit()          
        #9
        print("SUA VEZ")
        jogadaPlayer(tabuleiro, simboloPlayer) 
        verificaJogada(tabuleiro)        
        if verificaJogada(tabuleiro) == True:
            print("Você venceu a partida!")
            _ = input("Pressione enter para finalizar...")
            exit() 
        else:
            print("Empate!!!")
            _ = input("Pressione enter para finalizar...")
            exit()                                  

## NÃO ALTERE O CÓDIGO ABAIXO ##
if __name__ == "__main__":
    main()