import pytest
from src.operations import filter_by_description, count_by_category


@pytest.fixture
def test_data():
    return [
        {'description': 'Перевод', 'status': 'EXECUTED'},
        {'description': 'Покупка', 'status': 'CANCELED'},
        {'description': 'Перевод', 'status': 'PENDING'},
    ]


def test_filter_desc(test_data):
    assert len(filter_by_description(test_data, 'перевод')) == 2
    assert len(filter_by_description(test_data, 'покупка')) == 1
    assert len(filter_by_description([], 'test')) == 0


def test_count_cat(test_data):
    cats = ['Перевод', 'Покупка', 'Продажа']
    assert count_by_category(test_data, cats) == {'Перевод': 2, 'Покупка': 1, 'Продажа': 0}
    assert count_by_category([], cats) == {}