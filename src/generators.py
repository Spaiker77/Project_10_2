from typing import Any, Generator


def filter_by_currency(transaktions: Any, code: str) -> list:
    """Генераторная функция, которая возвращает транзакции с заданной валютой."""
    for transaktion in transaktions:
        if transaktion["operationAmout"]["currency"]["code"] == code:
            yield transaktion


def transaction_descriptions(transactions: Any) -> Generator:
    """Генератор, который принимает список словарей
    с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start, stop):
    """Генератор, который выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    for number in range(start, stop + 1):
        # Форматируем номер карты в нужный формат XXXX XXXX XXXX XXXX
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[
            8:12
        ] + " " + f"{number:016d}"[12:16]
