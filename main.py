from bank_operations import *

menu = """
Bem vindo ao DIO Bank.

Selecione uma opção para continuar:

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Criar Cliente
[5] - Listar Clientes
[6] - Criar Conta Corrente
[7] - Listar contas correntes
[8] - Listar contas correntes por usuário
[0] - Sair
"""

# TODO Criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário)

print(menu)
while True:
    option = input("Digite a opção desejada: ")
    if option == '1':
        print("Opção selecionada: Depositar")
        amount = float(input("Digite o valor do deposito: "))
        try:
            deposit(amount)
        except ValueError as err:
            print(err)
        print(menu)

    elif option == '2':
        print("Opção selecionada: Sacar")
        amount = float(input("Digite o valor do saque: "))
        try:
            withdraw(amount=amount)
        except ValueError as err:
            print(err)

        print(menu)

    elif option == '3':
        print("Opção selecionada: Extrato")
        try:
            generate_statement()
        except (ValueError, TypeError) as err:
            print(err)

        print(menu)

    elif option == '4':
        print("Opção selecionada: Criar Cliente")
        try:
            add_new_client()
        except (ValueError, TypeError) as err:
            print(err)

        print(menu)

    elif option == '5':
        print("Opção selecionada: Listar Clientes")
        try:
            list_all_clients()
        except (ValueError, TypeError) as err:
            print(err)

        print(menu)

    elif option == '6':
        print("Opção selecionada: Criar Conta Corrente")
        client_id = input("Digite o CPF do cliente: ")
        try:
            add_new_account(client_id)
        except (ValueError, TypeError) as err:
            print(err)

        print(menu)

    elif option == '7':
        print("Opção selecionada: Listar todas as contas")
        try:
            list_all_accounts()
        except (ValueError, TypeError) as err:
            print(err)

        print(menu)

    elif option == '8':
        print("Opção selecionada: Listar todas as contas de um cliente específico.")
        client_id = input("Digite o CPF do cliente: ")
        try:
            list_accounts_by_client(client_id)
        except ValueError as err:
            print(err)

        print(menu)

    elif option == '0':
        print("Opção selecionada: Sair")
        break

    else:
        print("Opção inválida. Tente novamente.")
