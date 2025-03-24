from src.widget import mask_account_card, get_date
import pytest
from typing import List, Tuple

if __name__ == "__main__":
    pytest.main()


@pytest.fixture
def card_data() -> List[Tuple[str, str]]:
    return [
        ("Visa 1234567812345678", "Visa 1234 **** **** 5678"),
        ("MasterCard 1234567890123456", "MasterCard 1234 **** **** 3456"),  # Исправлено на 3456
        ("Account 12345678901234567890", "Account ****************7890"),
        ("Account 12345", "Account *****"),
    ]


def test_mask_account_card_with_card(card_data: List[Tuple[str, str]]) -> None:
    for input_data, expected_output in card_data[:2]:  # Тестируем только карты
        result = mask_account_card(input_data)
        assert result == expected_output, f"Expected: {expected_output}, but got: {result}"


def test_mask_account_card_with_account(card_data: List[Tuple[str, str]]) -> None:
    for input_data, expected_output in card_data[2:]:  # Тестируем только счета
        result = mask_account_card(input_data)
        assert result == expected_output, f"Expected: {expected_output}, but got: {result}"


@pytest.fixture
def date_data() -> List[Tuple[str, str]]:
    return [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-25T15:00:00.000000", "25.12.2023"),
        ("2020-01-01T00:00:00.000000", "01.01.2020"),
        ("2019-07-04T10:20:30.123456", "04.07.2019"),
    ]


def test_get_date(date_data: List[Tuple[str, str]]) -> None:
    for input_date, expected_output in date_data:
        result = get_date(input_date)
        assert result == expected_output
