import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

account_balance = 0.0
MAX_WITHDRAW_LIMIT = 3
MAX_WITHDRAW_AMOUNT = 500.0
current_withdraw_amount = 0
bank_statement = []
clients = []
accounts = []

# TODO A Conta Corrente deve conter as seguintes informações: agência, numero e usuário
#  O numero da conta é sequencial e deve começar em 1. O número da agência é fixo. Um usuário pode ter
#  mais de uma conta, mas cada conta só pode ter um usuário

"""
{
    account_id: 1
    account_branch: '0056'
    account_holder: 123456789
    account_balance
}
"""


def list_accounts_by_client(client_id: str) -> None:
    pass


def list_all_accounts() -> None:
    pass


def add_new_account() -> None:
    pass


def create_account(client_id: str) -> dict:
    if not check_if_client_exists(client_id):
        raise ValueError("Esse CPF não existe em nossa base de clientes.")

    account_id = 1 if len(clients) == 0 else len(clients) + 1
    account_branch = '0056'
    account_holder = client_id
    account_balance = 0.0
    account = {'account_id': account_id, 'account_branch': account_branch, 'account_holder': account_holder,
               'account_balance': account_balance}
    return account


def list_all_clients() -> None:
    """
    This function prints all clients in `clients` list to the console.
    :return: Nothing.
    """

    for client in clients:
        print(client)


def add_new_client() -> None:
    """
    This function calls the `create_client` function to create a new client and then append it to the
    `clients` list.

    :return: Nothing
    """
    try:
        new_client = create_client()
        clients.append(new_client)

        print("Cliente adicionado com sucesso!")

    except (TypeError, ValueError) as err:
        print(err)


def create_client() -> dict:
    """
    This function will create a new client for the banking system. It prompts the user for the client data and returns
    a dictionary of it.

    :return: A dictionary of client's data.
    """
    client_id = input("Insira o CPF do usuário: ").strip(" ./-")

    if check_if_client_exists(client_id):
        raise ValueError("Erro ao criar cliente: CPF já cadastrado.")

    client_name = input("Insira o nome do usuário: ").strip()
    client_birth = input("Insira a data de nascimento do usuário: ").strip()
    client_address = create_client_address()

    client = {'client_id': client_id, 'client_name': client_name, 'client_birth': client_birth,
              'client_address': client_address}
    return client


def check_if_client_exists(client_id: str) -> bool:
    """
    This function checks if the client_id (the CPF number) exists anywhere in the `clients` list. If such
    data is found, the function returns `True`. Else, it returns `False`.
    This is needed because the client_id must be exclusive.

    :param client_id: The client ID (their CPF number)
    :return: `True` if the data is found, `False` otherwise
    """
    for client in clients:
        if client_id in client.values():
            return True
    return False


def create_client_address() -> str:
    """
    This function prompts the user for the client address details and returns a formatted string of the address.

    :returns: A string of the client's address.
    """
    client_address_street = input("Insira o nome da rua: ").strip()
    client_address_number = input("Insira o número do endereço: ").strip()
    client_address_neighborhood = input("Insira o bairro: ").strip()
    client_address_city = input("Insira a cidade: ").strip()
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
