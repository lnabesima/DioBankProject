from bank_operations import deposit, withdraw, generate_statement

menu = """
Bem vindo ao DIO Bank.

Selecione uma opção para continuar:

[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair
"""

# TODO Criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário)
# TODO O usuário deve conter as seguintes informações: nome, data de nascimento, cpf e endereço.
#  O endereço é uma string que contém os seguintes dados: logradouro, numero, bairro, cidade/estado
#  O CPF deve ser único e armazenado somente os números. Os usuários devem ser armazenados em uma lista
# TODO A Conta Corrente deve conter as seguintes informações: agência, numero e usuário
#  O numero da conta é sequencial e deve começar em 1. O número da agência é fixo. Um usuário pode ter
#  mais de uma conta, mas cada conta só pode ter um usuário


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
    elif option == '0':
        print("Opção selecionada: Sair")
        break
    else:
        print("Opção inválida. Tente novamente.")
