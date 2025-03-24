import logging
from typing import Union

# Настройка логгера
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)


# Настройка обработчика файла
file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_handler.setLevel(logging.DEBUG)

# Настройка форматера
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    try:
        # Убедимся, что номер карты состоит только из цифр
        original_number = card_number
        card_number = "".join(filter(str.isdigit, card_number))

        if not card_number:
            logger.error("Empty card number provided")
            return original_number

        if len(card_number) >= 16:
            result = f"{card_number[:4]} {card_number[4:6]} **** {card_number[-4:]}"
        elif len(card_number) < 16 and len(card_number) >= 8:
            result = f"{card_number[:4]}{'*' * (len(card_number) - 8)} **** {card_number[-4:]}"
        elif len(card_number) < 8:
            result = f"{card_number[:4]} **** "
        else:
            result = card_number

        logger.debug(f"Successfully masked card number: {original_number} -> {result}")
        return result

    except Exception as e:
        logger.error(f"Error masking card number: {card_number}. Error: {str(e)}")
        return card_number


def get_mask_account(account: Union[str]) -> Union[str]:
    """Функция принимает на вход номер счета и возвращает его маску"""
    try:
        if not account:
            logger.error("Empty account number provided")
            return account

        result = f"** {account[-4:]}"
        logger.debug(f"Successfully masked account: {account} -> {result}")
        return result

    except Exception as e:
        logger.error(f"Error masking account: {account}. Error: {str(e)}")
        return account


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430133874305"))
