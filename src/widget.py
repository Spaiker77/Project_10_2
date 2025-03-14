import datetime
from typing import Union


def mask_account_card(account_info: str) -> str:
    parts = account_info.split()
    card_type = parts[0]
    number = parts[1]

    # Определяем длину номера и маскируем его
    if len(number) == 16:  # Для карт
        masked_number = f"{number[:4]} **** **** {number[-4:]}"
    elif len(number) >= 12:  # Для аккаунтов (может быть больше 12 цифр)
        masked_number = "*" * (len(number) - 4) + number[-4:]
    else:  # Если номер короткий, просто маскируем его
        masked_number = "*" * len(number)

    return f"{card_type} {masked_number}"


def get_date(user_date: Union[str]) -> Union[str]:
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")."""

    date_format = datetime.datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")

    return new_date


print(mask_account_card("Visa Platinum 1234567891234567"))
print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024
