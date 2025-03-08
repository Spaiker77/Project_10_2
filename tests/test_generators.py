from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
import pytest
from typing import Any, List, Generator


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

# Фикстуры для тестов


@pytest.fixture
def sample_transactions():
    return [
        {"operationAmout": {"amount": 100, "currency": {"code": "USD"}}},
        {"operationAmout": {"amount": 200, "currency": {"code": "EUR"}}},
    ]


@pytest.fixture
def card_number_range():
    return (4000000000000000, 4000000000000003)


# Тест для функции test_filter_by_currency
def test_filter_by_currency(sample_transactions):
    # Получаем первый элемент с валютой USD
    result = next(filter_by_currency(sample_transactions, "USD"), None)
    expected = {"operationAmout": {"amount": 100, "currency": {"code": "USD"}}}
    assert result == expected


# Тест для генератора transaction_descriptions
def test_transaction_descriptions():
    sample_transactions = [
        {"operationAmount": 100, "description": "Payment for groceries", "currency": "USD"},
        {"operationAmount": 150, "description": "Payment for utilities", "currency": "USD"},
        {"operationAmount": 200, "description": "Payment for rent", "currency": "USD"},
    ]

    # Создаем генератор
    descriptions = transaction_descriptions(sample_transactions)

    # Проверяем каждое описание по очереди
    assert next(descriptions) == "Payment for groceries"
    assert next(descriptions) == "Payment for utilities"
    assert next(descriptions) == "Payment for rent"

    # Проверка на окончание генератора
    try:
        next(descriptions)
        assert False, "Expected StopIteration exception"
    except StopIteration:
        pass  # Ожидаем исключение StopIteration, когда генератор исчерпан


# Тест для card_number_generator:
def test_card_number_generator():
    # Тестируем диапазон от 0 до 2
    generator = card_number_generator(0, 2)

    # Проверяем первые три значения генератора
    assert next(generator) == "0000 0000 0000 0000"  # 0000000000000000
    assert next(generator) == "0000 0000 0000 0001"  # 0000000000000001
    assert next(generator) == "0000 0000 0000 0002"  # 0000000000000002

    # Проверка на окончание генератора
    try:
        next(generator)
        assert False, "Expected StopIteration exception"
    except StopIteration:
        pass  # Ожидаем исключение StopIteration, когда генератор исчерпан
