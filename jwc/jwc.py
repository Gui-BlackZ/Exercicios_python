#Solicita nome do titular
nome_titular = input("Informe o nome da conta do titular: ")

#Abetura da conta(Deposito inicial)
while True:
    deposito_inicial = input("Digite o valor de deposito inicial: ")
    if deposito_inicial.replace(".","",1).isdigit():
        deposito_inicial = float(deposito_inicial)
        if deposito_inicial >= 0:
            conta = (nome_titular, [deposito_inicial],[])
            
            break
        else:
            print("Valor Inválido! Digite um número")
    else:
        print("Valor Inválido! Digite um numero:")

#Operções (Depositar, Sacar, Consultar saldo, Consultar historico, sair)

while True:     
    print("----Escolha uma operação:---")
    print("\n1-Depositar \n2-Sacar \n3-Cosultar saldo \n4-Consultar histórico \n5-sair ")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        while True:
            valor_deposito = input("Digite um valor de deposito: ")
            if valor_deposito.replace(".","",1).isdigit():
                valor_deposito = float(valor_deposito)
                if valor_deposito >= 0:
                    #valor_deposito += conta[1][0]
                    #Soma o valor do saldo
                    conta[1][0] += valor_deposito
                    #Adicona ao historico
                    conta[2].append(f"Depósito de R$: {valor_deposito} ")
                    print("\nDeposito realizado com sucesso\n")
                    break
                else:
                    print("Valor invalido.")
            else: 
                print("Entrada invalida. Digite um número.")
    elif opcao == "2":
        print("Sacar")
        while True:
            valor_deposito = input("Digite um valor de saque: ")
            if valor_deposito.replace(".","",1).isdigit():
                valor_deposito = float(valor_deposito)
                if valor_deposito >= 0:
                    if valor_deposito <= conta[1][0]:
                        conta[1][0] -= valor_deposito
                        conta[2].append(f"Saque de R$: {valor_deposito}")
                        print("\nSaque realizado com sucesso\n")
                        break
                    else:
                        print("Valor inválido.")
                else:
                    print("Entrada inválida. Digite um número.")
    elif opcao == "3":
        print(f"\nSaldo atual: R$ {conta[1][0]:.2f}\n")
            
    elif opcao == "4":
        print("Historico")
        if conta[2]:
            for item in conta[2]:
                print(f" - {item}")
    elif opcao == "5":
        print("Obrigado por usar nosso Banco.")
        break
    else: 
        print("Opção Invalida. Por favor, escolha uma opção do menu.")

    