from os import system, name

def limpaTela(): 
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear')

def deposito(valorDeposito = 0, n100 = 0, n50 = 0, n20 = 0, n10 = 0, n5 = 0, n2 = 0, n1 = 0):
    """
    A função 'deposito' permite o usuário inserir cédulas de dinheiro no cofrinho digital e retorna o valor de depósito
    e a quantidade de notas de cada valor inserida.
    """    
    valor = int(input("Insira uma nota:R$"))
    if valor < 0:
        return valorDeposito, n100, n50, n20, n10, n5, n2, n1
    elif valor == 0:
        print("Insira um valor maior que 0!")
        return deposito(valorDeposito, n100, n50, n20, n10, n5, n2, n1)
    elif valor != 100 and valor != 50 and valor != 20 and valor != 10 and valor != 5 and valor != 2 and valor != 1:
        print("NOTA DESCONHECIDA!")
        return deposito(valorDeposito, n100, n50, n20, n10, n5, n2, n1)
    else:
        if valor == 100:
            n100 += 1
        elif valor == 50:
            n50 += 1
        elif valor == 20:
            n20 += 1
        elif valor == 10:
            n10 += 1
        elif valor == 5:
            n5 += 1
        elif valor == 2:
            n2 += 1
        elif valor == 1:
            n1 += 1
        return deposito(valorDeposito + valor, n100, n50, n20, n10, n5, n2, n1)

def saque(saldo, nota100, nota50, nota20, nota10, nota5, nota2, nota1):
    """
    A função 'saque' mostra a quantidade de notas disponíveis para saque, e lê o valor que o usuário quer sacar,
    caso a quantia for positiva, a função retorna esse falor que será usado posteriormente na função 'cofrinho'.
    Caso o valor lido seja negativo, será exibido um aviso de valor inválido e a função será executada novamente.
    """    
    print("NOTAS DISPONÍVEIS PARA SAQUE:")
    print("-----------------------------")
    if nota100 > 0:
        print(f"{nota100} x R$100,00")
    if nota50 > 0:
        print(f"{nota50} x R$50,00")
    if nota20 > 0:
        print(f"{nota20} x R$20,00")
    if nota10 > 0:
        print(f"{nota10} x R$10,00")
    if nota5 > 0:
        print(f"{nota5} x R$5,00")   
    if nota2 > 0:
        print(f"{nota2} x R$2,00")
    if nota1 > 0: 
        print(f"{nota1} x R$1,00")      
    
    print("-----------------------------")
    
    valor1 = float(input("DIGITE O VALOR PARA SAQUE:" ))
    
    if valor1 > 0:
        return valor1
    elif valor1 == 0:
        print("DIGITE UM VALOR MAIOR QUE 0")
        return saque(saldo, nota100, nota50, nota20, nota10, nota5, nota2, nota1)        
    else:
        print("VALOR INVÁLIDO")
        return saque(saldo, nota100, nota50, nota20, nota10, nota5, nota2, nota1)

def saqueNotas(valorNotas, nota100, nota50, nota20, nota10, nota5, nota2, nota1, not100 = 0, not50 = 0, not20 = 0, not10 = 0, not5 = 0, not2 = 0, not1 = 0):
    """
    A função 'saqueNotas' atualiza a quantidade de notas de cada valor após um saque de acordo com o estoque de notas do usuário.
    Depois ele retorna a nova quantidade de notas que será usado no relatório.
    """
    n = 0
    if valorNotas >= 100 and nota100 > 0:
        print("R$100,00")
        return saqueNotas(valorNotas - 100, nota100 - 1, nota50, nota20, nota10, nota5, nota2, nota1, not100 + 1)
    elif valorNotas >= 50 and nota50 > 0:
        print("R$50,00")
        return saqueNotas(valorNotas - 50, nota100, nota50 - 1, nota20, nota10, nota5, nota2, nota1, not100, not50 + 1)
    elif valorNotas >= 20 and nota20 > 0:
        print("R$20,00")
        return saqueNotas(valorNotas - 20, nota100, nota50, nota20 -1, nota10, nota5, nota2, nota1, not100, not50, not20 + 1)
    elif valorNotas >= 10 and nota10 > 0:
        print("R$10,00")
        return saqueNotas(valorNotas - 10, nota100, nota50, nota20, nota10 - 1, nota5, nota2, nota1, not100, not50, not20, not10 + 1)
    elif valorNotas >= 5 and nota5 > 0:
        print("R$5,00")
        return saqueNotas(valorNotas - 5, nota100, nota50, nota20, nota10, nota5 - 1, nota2, nota1, not100, not50, not20, not10, not5 + 1)
    elif valorNotas >= 2 and nota2 > 0:
        print("R$2,00")
        return saqueNotas(valorNotas - 2, nota100, nota50, nota20, nota10, nota5, nota2 - 1, nota1, not100, not50, not20, not10, not5, not2 + 1)
    elif valorNotas >= 1 and nota1 > 0:
        print("R$1,00")
        return saqueNotas(valorNotas - 1, nota100, nota50, nota20, nota10, nota5, nota2, nota1 - 1, not100, not50, not20, not10, not5, not2, not1 + 1)
    elif valorNotas > 0:
        n += 1
    return n, not100, not50, not20, not10, not5, not2, not1

def printNotas(saldo):
    """
    Imprime o valor sacado
    """
    print(f"Valor Sacado: R${saldo:.2f}")
    print("RETIRE SEU DINHEIRO:")

def cofrinho(saldo = 188, nota100 = 1, nota50 = 1, nota20 = 1, nota10 = 1, nota5 = 1, nota2 = 1, nota1 = 1):
    """
    A função cofrinho é a função geral que chama e organiza todas as outras funções do código
    A função possuí um menu com uma opção de escolha de 1 a 5 para iniciar uma tarefa do programa.
    Nela serão chamadas as funções de depósito, saque, saldo e relatório, além de se poder finalizar o programa.
    """    
    limpaTela()
    print("+--------------------------------------------------+")
    print("|                                                  |")            
    print("| 1 - Depositar                                    |")
    print("| 2 - Sacar                                        |")
    print("| 3 - Saldo                                        |")
    print("| 4 - Relatório                                    |")
    print("| 5 - Sair                                         |")
    print("|                                                  |")
    print("+--------------------------------------------------+")
    print("......POR FAVOR, ESCOLHA UMA DAS OPÇÕES ACIMA:......")
    
    x = int(input())
    if x <= 0 or x >= 6:
        _ = input("Opção inválida! aperte ENTER para retornar...")
        return cofrinho()
    
    elif x == 5:
        limpaTela()
        if saldo > 0:
            opcao1 = input("Deseja sacar seu saldo antes de finalizar (S/N)? ")
            if opcao1 == "N" or opcao1 == "n":
                print("VOCÊ SAIU DO PROGRAMA")
                exit()
            elif opcao1 == "S" or opcao1 == "s":
                printNotas(saldo)
                saqueNotas(saldo, nota100, nota50, nota20, nota10, nota5, nota2, nota1)
                _ = input("Pressione a tecla ENTER para finalizar... ")
                print("O PROGRAMA ENCERROU")
                exit()
            else:
                print("Opção invalida")
                _ = input("Pressione a tecla ENTER para continuar... ")    
                cofrinho(saldo, nota100, nota50, nota20, nota10, nota5, nota2, nota1)                
        else:
            print("VOCÊ SAIU DO PROGRAMA")
            exit()                
    
    elif x == 1:
        print("-- DEPÓSITO --")
        print("Para terminar o depósito coloque um valor negativo")        
        valorDeposito, n100, n50, n20, n10, n5, n2, n1 = deposito()
        print(f"Valor depositado: R${valorDeposito:.2f}")
        print(f"Notas de R$ 100,00: {n100}")
        print(f"Notas de R$ 50,00: {n50}")
        print(f"Notas de R$ 20,00: {n20}")
        print(f"Notas de R$ 10,00: {n10}")
        print(f"Notas de R$ 5,00: {n5}")
        print(f"Notas de R$ 2,00: {n2}")
        print(f"Notas de R$ 1,00: {n1}")
        _ = input("Pressione a tecla ENTER para continuar... ")
        cofrinho(saldo + valorDeposito, nota100 + n100, nota50 + n50, nota20 + n20, nota10 + n10, nota5 + n5, nota2 + n2, nota1 + n1)
    
    elif x == 2:
        print("+--------------------------------+")
        print("|              SAQUE             |")
        print("+--------------------------------+")         
        if saldo > 0:
            valor1 = saque(saldo, nota100, nota50, nota20, nota10, nota5, nota2, nota1)
            if valor1 > saldo:
                print("VOCÊ NÃO POSSUI SALDO SUFICIENTE!")
                valor1 = 0
                opcao = (input(f"Você possui R${saldo:.2f} no cofrinho, deseja sacar(S/N)? "))
                if opcao == "N" or opcao == "n":
                    _ = input("Pressione a tecla ENTER para continuar... ")    
                    cofrinho(saldo, nota100, nota50, nota20, nota10, nota5, nota2, nota1)                    
                elif opcao == "S" or opcao == "s":
                    printNotas(saldo)               
                    saqueNotas(saldo, nota100, nota50, nota20, nota10, nota5, nota2, nota1)              
                    _ = input("Pressione a tecla ENTER para continuar... ")
                    cofrinho(saldo = 0, nota100 = 0, nota50 = 0, nota20 = 0, nota10 = 0, nota5 = 0, nota2 = 0, nota1 = 0)
                elif opcao != "N" or opcao != "n" or opcao != "S" or opcao != "s":
                    print("Opção invalida")
                    _ = input("Pressione a tecla ENTER para continuar... ")    
                    cofrinho(saldo, nota100, nota50, nota20, nota10, nota5, nota2, nota1)                            
            elif valor1 <= saldo:
                printNotas(valor1)
                n, not100, not50, not20, not10, not5, not2, not1 = saqueNotas(valor1, nota100, nota50, nota20, nota10, nota5, nota2, nota1)
                if n == 0:
                    _ = input("Pressione a tecla ENTER para continuar... ")
                    cofrinho(saldo - valor1, nota100 - not100, nota50 - not50, nota20 - not20, nota10 - not10, nota5 - not5, nota2 - not2, nota1 - not1)                
                elif n == 1:
                    limpaTela()
                    print("O COFRINHO NÃO POSSUI NOTAS SUFICIENTES")
                    _ = input("Pressione a tecla ENTER para continuar... ")
                    cofrinho(saldo, nota100, nota50, nota20, nota10, nota5, nota2, nota1)
        
        else:
            print("VOCÊ NÃO POSSUÍ SALDO!")
        _ = input("Pressione a tecla ENTER para continuar... ")    
        cofrinho(saldo, nota100, nota50, nota20, nota10, nota5, nota2, nota1)
    
    elif x == 3:
        print(f"O SEU SALDO ATUAL É: R${saldo:.2f}")
        _ = input("Pressione a tecla ENTER para continuar... ")
        cofrinho(saldo, nota100, nota50, nota20, nota10, nota5, nota2, nota1)
    
    elif x == 4:
        print("+------------------------------------+")
        print("|              RELATÓRIO             |")
        print("+------------------------------------+")
        print(f"O SEU SALDO ATUAL É: R${saldo:.2f}")
        print(f"Notas de R$ 100,00: {nota100}")
        print(f"Notas de R$ 50,00: {nota50}")
        print(f"Notas de R$ 20,00: {nota20}")
        print(f"Notas de R$ 10,00: {nota10}")
        print(f"Notas de R$ 5,00: {nota5}")
        print(f"Notas de R$ 2,00: {nota2}")
        print(f"Notas de R$ 1,00: {nota1}") 
        _ = input("Pressione a tecla ENTER para continuar... ")       
        cofrinho(saldo, nota100, nota50, nota20, nota10, nota5, nota2, nota1)

def main():
    cofrinho()

main()