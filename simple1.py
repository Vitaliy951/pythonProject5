ef get_mask_account(account_number: str) -> str:
    """Удаление пробелов"""
    account_number = account_number.replace(" ", "")

    """ Проверка, что ввод состоит только из цифр"""
    if not account_number.isdigit():
        raise ValueError("Номер счета должен состоять только из цифр.")

    """ Форматирование номера счета"""
    masked_account = f"**{account_number[-4:]}"
    return masked_account