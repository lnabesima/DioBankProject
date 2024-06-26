from bank_operations import deposit

import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

menu = """
Bem vindo ao DIO Bank.

Selecione uma opção para continuar:

[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair
"""

account_balance = 0.0
MAX_WITHDRAW_LIMIT = 3
MAX_WITHDRAW_AMOUNT = 500.0
current_withdraw_amount = 0
bank_statement = []

# TODO Separar as opções do menu em funções separadas
# TODO A função `saque` deve receber parâmetros apenas por argumentos nomeados
# TODO A função `extrato` deve receber parâmetros por argumentos posicionais E nomeados
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
        except (ValueError, TypeError) as err:
            print(err)
        print(menu)

    elif option == '2':
        print("Opção selecionada: Sacar")
        if current_withdraw_amount >= MAX_WITHDRAW_LIMIT:
            print("Você atingiu o limite máximo de saques diários. Tente novamente amanhã.")
            print(menu)
            continue

        amount = float(input("Digite o valor do saque: "))
        if amount > MAX_WITHDRAW_AMOUNT:
            print(f"O valor é maior do que o limite máximo de saque por operação.")
            continue

        if account_balance > amount:
            account_balance -= amount
            current_withdraw_amount += 1
            bank_statement.append(f"Saque: {locale.currency(amount)}")
            print(
                f"Saque de {locale.currency(amount)} realizado com sucesso. "
                f"Saldo atual: {locale.currency(account_balance)}")
            print(menu)
        else:
            print("Seu saldo é insuficiente para realizar esta operação.")
            print(menu)

    elif option == '3':
        print("Opção selecionada: Extrato")
        if not bank_statement:
            print("Não foram registradas transações nesta conta.")
            continue

        for transaction in bank_statement:
            print(transaction)
        print(f"Saldo atual: {locale.currency(account_balance)}")
        print(menu)
    elif option == '0':
        print("Opção selecionada: Sair")
        break
    else:
        print("Opção inválida. Tente novamente.")
