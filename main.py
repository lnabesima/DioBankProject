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
current_withdraw_amount = 0

print(menu)
while True:
    option = input("Digite a opção desejada: ")
    if option == '1':
        print("Opção selecionada: Depositar")
        amount = float(input("Digite o valor do deposito: "))
        account_balance += amount
        print(
            f"Depósito de {locale.currency(amount)} realizado com sucesso. Saldo atual: {locale.currency(account_balance)}")
        print(menu)

    elif option == '2':
        print("Opção selecionada: Sacar")
        if current_withdraw_amount >= MAX_WITHDRAW_LIMIT:
            print("Você atingiu o limite máximo de saques diários. Tente novamente amanhã.")
            break

        amount = float(input("Digite o valor do saque: "))
        if account_balance > amount:
            account_balance -= amount
            print(
                f"Saque de {locale.currency(amount)} realizado com sucesso. "
                f"Saldo atual: {locale.currency(account_balance)}")
            print(menu)
        else:
            print("Seu saldo é insuficiente para realizar esta operação.")
            print(menu)

    elif option == '3':
        print("Opção selecionada: Extrato")
    elif option == '0':
        print("Opção selecionada: Sair")
        break
    else:
        print("Opção inválida. Tente novamente.")
