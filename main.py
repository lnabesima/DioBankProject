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

print(menu)
while True:
    option = input("Digite a opção desejada: ")
    if option == '1':
        print("Opção selecionada: Depositar")
        amount = float(input("Digite o valor do deposito: "))
        if amount <= 0:
            print(f"Valor inválido. Por favor tente novamente.")
            continue
        account_balance += amount
        bank_statement.append(f"Depósito: {locale.currency(amount)}")
        print(
            f"Depósito de {locale.currency(amount)} realizado com sucesso. Saldo atual: {locale.currency(account_balance)}")
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
