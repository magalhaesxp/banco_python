menu= """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    if opcao =='d':
        print("Deposito")
        deposito = float(input('Informe o valor do deposito:'))
        if deposito > 0:
            saldo += deposito
            extrato += f'Deposito: R$ {deposito:.2f}\n'
        else:
            print("valor insuficiente")

    elif opcao == 's':
        print('Saque')
        if numero_saques <= 3:
            print("Informe valor do saque:")
            saque = float(input('Valor desejado:'))

            if saque > saldo:
                print('Saldo insuficente')
            elif saque > 500:
                print('Valor acima do limite')
            elif saque > 0:
                saldo -= saque
                numero_saques += 1
                extrato += f'Saque: R$ {saque:.2f}\n'
        else:
             print('excedeu o numero de saques')   
    elif opcao == 'e':
        print('Extrato')
        print(extrato)
        print('Limite', limite)
        print(f'Saldo R$ {saldo:.2f}')


    elif opcao == 'q':
        break
