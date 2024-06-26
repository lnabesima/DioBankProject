import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

account_balance = 0.0
MAX_WITHDRAW_LIMIT = 3
MAX_WITHDRAW_AMOUNT = 500.0
current_withdraw_amount = 0
bank_statement = []
users = []

# TODO O usuário deve conter as seguintes informações: nome, data de nascimento, cpf e endereço.
#  O endereço é uma string que contém os seguintes dados: logradouro, numero, bairro, cidade/estado
#  O CPF deve ser único e armazenado somente os números. Os usuários devem ser armazenados em uma lista

"""
{
    user_id: CPF
    user_name: John Doe
    user_birth: 01/01/1973
    user_address: Rua dos Bobos, 01, Centro, São Paulo/SP
}
"""


def create_client() -> dict:
    """
    This function will create a new client for the banking system. It prompts the user for the client data and returns
    a dictionary of it.

    :return: A dictionary of client's data.
    """
    client_id = input("Insira o CPF do usuário: ").strip(" ./-")
    client_name = input("Insira o nome do usuário: ").strip()
    client_birth = input("Insira a data de nascimento do usuário: ").strip()
    client_address = create_client_address()

    client = {
        'client_id': client_id,
        'client_name': client_name,
        'client_birth': client_birth,
        'client_address': client_address
    }
    return client


def create_client_address() -> str:
    """
    This function prompts the user for the client address details and returns a formatted string of the address.

    :returns: A string of the client's address.
    """
    client_address_street = input("Insira o nome da rua: ").strip()
    client_address_number = input("Insira o número do endereço: ").strip()
    client_address_neighborhood = input("Insira o bairro: ").strip()
    client_address_city = input("Insira a cidade/: ").strip()
    client_address_state = input("Insira a sigla da UF: ").strip()
    client_address = (
        f"{client_address_street}, {client_address_number}, {client_address_neighborhood}, {client_address_city}/"
        f"{client_address_state}")

    return client_address


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
