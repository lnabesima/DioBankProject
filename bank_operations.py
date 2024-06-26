import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

account_balance = 0.0
MAX_WITHDRAW_LIMIT = 3
MAX_WITHDRAW_AMOUNT = 500.0
current_withdraw_amount = 0
bank_statement = []


def withdraw(amount: float):
    global current_withdraw_amount, account_balance

    if current_withdraw_amount >= MAX_WITHDRAW_LIMIT:
        raise ValueError("Erro ao realizar saque: Limite máximo de saques atingido.")

    if amount > MAX_WITHDRAW_AMOUNT:
        raise ValueError(f"Erro ao realizar saque: O valor máximo de saque é {locale.currency(MAX_WITHDRAW_AMOUNT)}.")

    if amount > account_balance:
        raise ValueError("Erro ao realizar saque: Saldo insuficiente.")

    account_balance -= amount
    current_withdraw_amount += 1
    bank_statement.append(f"Saque: {locale.currency(amount)}")
    print(f"Saque de {locale.currency(amount)} realizado com sucesso. Saldo atual: {locale.currency(account_balance)}")
    return


def deposit(amount: float):
    global account_balance, bank_statement

    if amount < 0:
        raise ValueError(
            f"Erro ao realizar depósito: O valor a ser depositado precisa ser maior do que {locale.currency(0)}.")

    account_balance += amount
    bank_statement.append(f"Depósito: {locale.currency(amount)}")
    print(
        f"Depósito de {locale.currency(amount)} realizado com sucesso. Saldo atual: {locale.currency(account_balance)}")
    return


def generate_statement():
    if not bank_statement:
        print(f"Não foram registradas transações nesta conta.")

    for transaction in bank_statement:
        print(transaction)

    print(f"=== Saldo atual: {locale.currency(account_balance)} ===")
    return
