from bank_operations import deposit, withdraw, generate_statement, add_new_client, list_all_clients

menu = """
Bem vindo ao DIO Bank.

Selecione uma opção para continuar:

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Criar Cliente
[5] - Listar Clientes
[6] - Criar Conta Corrente
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
        generate_statement()
        print(menu)

    elif option == '4':
        print("Opção selecionada: Criar Cliente")
        add_new_client()

        print(menu)

    elif option == '5':
        print("Opção selecionada: Listar Clientes")
        list_all_clients()

        print(menu)

    elif option == '0':
        print("Opção selecionada: Sair")
        break

    else:
        print("Opção inválida. Tente novamente.")
