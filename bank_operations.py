import locale
import re

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

MAX_WITHDRAW_LIMIT = 3
MAX_WITHDRAW_AMOUNT = 500.0
clients = []
accounts = []


def list_accounts_by_client(client_id: str) -> None:
    """
    Prints all accounts that matches the ``client_id`` value in ``accounts`` list to the console. If it doesn't find
    any, it prints a message informing that specific client doesn't have any accounts.

    :param client_id: The client CPF, used as ID.
    :return: Nothing
    """

    clean_client_id = strip_special_chars(client_id)
    found_match = False

    for account in accounts:
        if account['account_holder'] == clean_client_id:
            print(account)
            found_match = True

    if not found_match:
        print("Não há contas cadastradas para esse cliente.")


def list_all_accounts() -> None:
    """
    This function prints all accounts in ``accounts`` list to the console.
    :return: Nothing.
    """
    if not accounts:
        print("Não há contas cadastradas.")
        return

    for account in accounts:
        print(account)


def add_new_account(client_id: str) -> None:
    """
    This function calls the ``create_account`` function to create a new client and then append it to the
    ``accounts`` list.

    :return: Nothing
    """
    clean_client_id = strip_special_chars(client_id)
    try:
        new_account = create_account(clean_client_id)
        accounts.append(new_account)

        print(f"Nova conta para cliente {client_id} criada com sucesso! Conta número {new_account.get('account_id')}")
    except (ValueError, TypeError) as err:
        print(err)


def create_account(client_id: str) -> dict:
    """
    Creates a new account using the ``client_id`` parameter. Initially all accounts have 0 as balance, '0056' as branch
    number and the account id is sequential. The ``client_id`` is used to assign the holder of the newly created account
    :param client_id: The ID of the account holder
    :return: A dictionary containing the data for the new account
    """
    if not check_if_client_exists(client_id):
        raise ValueError("Esse CPF não existe em nossa base de clientes.")

    account_id = 1 if len(accounts) == 0 else len(accounts) + 1
    account_branch = '0056'
    account_holder = client_id
    account_current_balance = 0.0
    account_current_withdraw_amount = 0
    account_statement = []
    account = {'account_id': account_id, 'account_branch': account_branch, 'account_holder': account_holder,
               'account_balance': account_current_balance,
               'account_current_withdraw_amount': account_current_withdraw_amount,
               'account_statement': account_statement}
    return account


def list_all_clients() -> None:
    """
    This function prints all clients in `clients` list to the console.
    :return: Nothing.
    """
    if not clients:
        print("Não há clientes cadastrados.")
        return

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
    client_id = strip_special_chars(input("Insira o CPF do usuário: ").strip(" ./-"))

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
    data is found, the function returns ``True``. Else, it returns ``False``.
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


def strip_special_chars(input_str: str) -> str:
    """
    This function leverages the ``re`` module to use a regex to strip all the dots, slashes and hyphens
    from a string, specially the ``client_id`` (which uses the CPF number, often inputted with all those
    symbols)

    :param input_str: The string that's going to be cleaned
    :return: The same string, but without dots, slashes and hyphens
    """
    return re.sub(r'[./-]', '', input_str)


def withdraw(amount: float, account_id: int) -> None:
    for account in accounts:
        if account['account_id'] == account_id:
            if account['account_current_withdraw_amount'] >= MAX_WITHDRAW_LIMIT:
                raise ValueError("Erro ao realizar saque: Limite máximo de saques atingido.")

            if amount > MAX_WITHDRAW_AMOUNT:
                raise ValueError(
                    f"Erro ao realizar saque: O valor máximo de saque é {locale.currency(MAX_WITHDRAW_AMOUNT)}.")

            if amount > account['account_balance']:
                raise ValueError("Erro ao realizar saque: Saldo insuficiente.")

            account['account_balance'] -= amount
            account['account_current_withdraw_amount'] += 1
            account['account_statement'].append(f"Saque: {locale.currency(amount)}")
            print(
                f"Saque de {locale.currency(amount)} realizado com sucesso. Saldo atual: "
                f"{locale.currency(account['account_balance'])}"
            )
            return

    raise ValueError("Não existe uma conta com esse número.")


def deposit(amount: float, account_id: int) -> None:
    for account in accounts:
        if account['account_id'] == account_id:
            if amount < 0:
                raise ValueError(
                    f"Erro ao realizar depósito: O valor a ser depositado precisa ser maior do que "
                    f"{locale.currency(0)}.")

            account['account_balance'] += amount
            account['account_statement'].append(f"Depósito: {locale.currency(amount)}")
            print(
                f"Depósito de {locale.currency(amount)} realizado com sucesso. Saldo atual: "
                f"{locale.currency(account['account_balance'])}"
            )
            return

    raise ValueError("Não existe uma conta com esse número.")


def generate_statement(account_id: int) -> None:
    for account in accounts:
        if account['account_id'] == account_id:

            if not account['account_statement']:
                print(f"Não foram registradas transações nesta conta.")

            for transaction in account['account_statement']:
                print(transaction)
            print(f"=== Saldo atual: {locale.currency(account['account_balance'])} ===")
            return

    raise ValueError("Não existe uma conta com esse número.")
