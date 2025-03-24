from unittest.mock import Mock, patch
from typing import Dict, Any
import src.external_api  # Импортируем модуль с функцией
import requests


# Тест для транзакции в рублях
def test_convert_rub() -> None:
    transaction: Dict[str, Any] = {"amount": 100.0, "currency": "RUB"}
    result = src.external_api.convert_transaction_amount(transaction)
    assert result == 100.0


# Тест для транзакции в неподдерживаемой валюте
def test_convert_unsupported_currency() -> None:
    transaction: Dict[str, Any] = {"amount": 100.0, "currency": "GBP"}
    result = src.external_api.convert_transaction_amount(transaction)
    assert result == 100.0


# Тест для транзакции в USD с обращением к API
@patch("requests.get")
def test_convert_usd_success(mock_get) -> None:
    # Настраиваем мок-ответ от API
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 75.5}}
    mock_get.return_value = mock_response

    transaction: Dict[str, Any] = {"amount": 100.0, "currency": "USD"}
    result = src.external_api.convert_transaction_amount(transaction)
    assert result == 7550.0  # 100 USD * 75.5 = 7550 RUB


# Тест для транзакции в EUR с ошибкой API
@patch("requests.get")
def test_convert_eur_api_failure(mock_get) -> None:
    # Настраиваем мок-ответ с ошибкой
    mock_response = Mock()
    mock_response.status_code = 500  # Симулируем ошибку сервера
    mock_response.json.return_value = {}  # Пустой ответ
    mock_get.return_value = mock_response

    transaction: Dict[str, Any] = {"amount": 100.0, "currency": "EUR"}
    result = src.external_api.convert_transaction_amount(transaction)
    assert result == 100.0  # Возвращена исходная сумма из-за ошибки API


# Тест для транзакции в USD с ошибкой KeyError в ответе API
@patch("requests.get")
def test_convert_usd_key_error(mock_get) -> None:
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {}
    mock_get.return_value = mock_response

    transaction: Dict[str, Any] = {"amount": 100.0, "currency": "USD"}
    result = src.external_api.convert_transaction_amount(transaction)
    assert result == 100.0


# Тест для транзакции в USD с ошибкой RequestException
@patch("requests.get")
def test_convert_usd_request_exception(mock_get) -> None:
    mock_get.side_effect = requests.RequestException("API недоступен")

    transaction: Dict[str, Any] = {"amount": 100.0, "currency": "USD"}
    result = src.external_api.convert_transaction_amount(transaction)
    assert result == 100.0