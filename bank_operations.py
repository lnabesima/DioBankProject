import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

account_balance = 0.0
bank_statement = []


def withdraw(amount: int):
    return


def deposit(amount: float):
    global account_balance
    global bank_statement

    if amount < 0:
        raise ValueError(
            f"Erro ao realizar depósito: O valor a ser depositado precisa ser maior do que {locale.currency(0)}.")

    account_balance += amount
    bank_statement.append(f"Depósito: {locale.currency(amount)}")
    print(
        f"Depósito de {locale.currency(amount)} realizado com sucesso. Saldo atual: {locale.currency(account_balance)}")

    return


def generate_statement():
    return
