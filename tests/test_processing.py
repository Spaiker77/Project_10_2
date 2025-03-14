from src.processing import filter_by_state, sort_by_date
import pytest
from typing import List, Dict, Any

if __name__ == "__main__":
    pytest.main()


# Фикстура для тестовых данных
@pytest.fixture
def list_of_dictionaries() -> List[Dict[str, Any]]:
    return [
        {"id": 41433829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 51428929, "state": "EXECUTED", "date": "2019-05-03T11:31:29.514464"},
        {"id": 47728829, "state": "CANCELED", "date": "2018-01-03T18:32:29.517764"},
        {"id": 12345678, "state": "EXECUTED", "date": "2020-01-01T12:00:00.000000"},  # Добавленная дата
    ]


# Тесты для функции filter_by_state
def test_filter_by_state(list_of_dictionaries: List[Dict[str, Any]]) -> None:
    result = filter_by_state(list_of_dictionaries, state="EXECUTED")
    assert len(result) == 4  # Должно вернуть 4 элемента
    assert all(item["state"] == "EXECUTED" for item in result)  # Все элементы должны иметь состояние EXECUTED


def test_filter_by_state_no_match(list_of_dictionaries: List[Dict[str, Any]]) -> None:
    result = filter_by_state(list_of_dictionaries, state="CANCELED")
    assert len(result) == 1  # Должно вернуть 1 элемент
    assert result[0]["state"] == "CANCELED"  # Элемент должен иметь состояние CANCELED


# Тесты для функции sort_by_date
def test_sort_by_date_descending(list_of_dictionaries: List[Dict[str, Any]]) -> None:
    result = sort_by_date(list_of_dictionaries, reverse=True)

    # Проверяем порядок дат (от самой поздней к самой ранней)
    assert result[0]["date"] == "2020-01-01T12:00:00.000000"
    assert result[1]["date"] == "2019-07-03T18:35:29.512364"
    assert result[2]["date"] == "2019-05-03T11:31:29.514464"
    assert result[3]["date"] == "2018-06-30T02:08:58.425572"
    assert result[4]["date"] == "2018-01-03T18:32:29.517764"


def test_sort_by_date_ascending(list_of_dictionaries: List[Dict[str, Any]]) -> None:
    result = sort_by_date(list_of_dictionaries, reverse=False)

    # Проверяем порядок дат (от самой ранней к самой поздней)
    assert result[0]["date"] == "2018-01-03T18:32:29.517764"
    assert result[1]["date"] == "2018-06-30T02:08:58.425572"
    assert result[2]["date"] == "2019-05-03T11:31:29.514464"
    assert result[3]["date"] == "2019-07-03T18:35:29.512364"
    assert result[4]["date"] == "2020-01-01T12:00:00.000000"
