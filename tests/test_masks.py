from src.masks import get_mask_account, get_mask_card_number
import pytest
from typing import List

if __name__ == "__main__":
    pytest.main()


# Фикстура для тестов
@pytest.fixture
def account_numbers() -> List[str]:
    return ["73654108430133874305", "12345678901234567890", "98765432109876543210"]


# Тесты для mask_account
def test_mask_account_standard(account_numbers: List[str]) -> None:
    account = account_numbers[0]
    masked = get_mask_account(account)
    assert masked == "** 4305"


def test_mask_account_another(account_numbers: List[str]) -> None:
    account = account_numbers[1]
    masked = get_mask_account(account)
    assert masked == "** 7890"


# Фикстура для тестов
@pytest.fixture
def card_data() -> str:
    return "1234567890123456"


@pytest.fixture
def short_card_data() -> str:
    return "1234"


# Тесты для get_mask_card_number
def test_get_mask_card_number(card_data: str) -> None:
    assert get_mask_card_number(card_data) == "1234 56** **** 3456"


def test_get_mask_card_number_short(short_card_data: str) -> None:
    assert get_mask_card_number(short_card_data) == "1234** **** "
