import textwrap

def menu():
    menu = """\n
    ==================== MENU ====================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tLista Conta
    [nu]\tNovo usuario 
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor,extrato, /):  ## A / aceita apenas valores por posição    
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    print(f'Deposito realizado:',valor)
    return saldo, extrato
    
def sacar(*,saldo, valor, extrato, limite, numero_saques,limite_saques): ## O * aceita apenas por passagem  
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    
    elif excedeu_saques :
        print("Operação falhou! Número máximo de saques excedido.")
    
    elif valor > 0:
        numero_saques += 1
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
                
        print(numero_saques, limite_saques)
    
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato


def imprime_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastro_usuario(usuarios):
    cpf = input('Digite o CPF (somente números:)')
    usuario = verifica_usuario(cpf,usuarios)
    if usuario:
        print('\nJá existe usuário com esse CPF!')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('informe a data de nascimento: (dd-mm-aaaa): ')
    endereco = input('Informe endereço (Rua, número - bairro - cidade / cigla estado): ')

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}) 
    print("Usuário criado com sucesso")

def verifica_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, conta, usuarios):
    cpf = input('Informe o CPFdo usuário:')
    usuario = verifica_usuario(cpf, usuarios)

    if usuario:
        print('\n=== Conta criada com sucesso! ===')
        return{"agencia": agencia, "numero_conta": conta, "usuario": usuario}
    
    print('\n @@@ Usuário não encontrado, fluxo de criação de conta finalizado@@@')

def exibir_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']} """

    print('=' * 100)
    print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    numero_saques = 0
    saldo = 0
    limite = 500
    extrato = ""
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao =='d':
            try:
                valor = float(input('Informe o valor do deposito:'))
                if valor > 0:
                    saldo, extrato = depositar(saldo, valor, extrato)
                else:
                    print('valor negativo, operação cancelada')
            except ValueError as ve:
                print('Valor diferente de número, operação cancelada')

        elif opcao == 's':
            valor = float(input('Informe o valor do saque:'))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor, 
                extrato=extrato, 
                limite=limite,
                numero_saques = numero_saques,  
                limite_saques=LIMITE_SAQUES)
                      
        elif opcao == 'e':
            
            imprime_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            cadastro_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            exibir_contas(contas)   

        elif opcao == 'q':
            break


main()
