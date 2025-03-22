import os
import requests
from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv()

API_KEY: str = os.getenv('API_LAYER_KEY', '')
BASE_URL: str = "https://api.apilayer.com/exchangerates_data/latest"


def convert_transaction_amount(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли. Для USD и EUR использует внешний API.
    Возвращает сумму в рублях как float.

    """
    amount: float = float(transaction.get('amount', 0))
    currency: str = transaction.get('currency', 'RUB').upper()

    if currency == 'RUB':
        print(f"Сумма в рублях: {amount} RUB")
        return amount

    if currency not in ('USD', 'EUR'):
        print(f"Валюта {currency} не поддерживается. Сумма: {amount}")
        return amount

    params: Dict[str, str] = {'base': currency, 'symbols': 'RUB'}
    headers: Dict[str, str] = {'apikey': API_KEY}

    try:
        response: requests.Response = requests.get(BASE_URL, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        rate: float = float(response.json()['rates']['RUB'])
        result: float = round(amount * rate, 2)
        print(f"Конвертация: {amount} {currency} → {result} RUB (курс: {rate})")
        return result
    except (requests.RequestException, KeyError) as e:
        print(f"Ошибка конвертации {currency}: {str(e)}. Возвращена исходная сумма")
        return amount