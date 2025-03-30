import json
import csv
from src.operations import filter_by_description
from typing import List, Dict

def load_json(file: str) -> List[Dict]:
    """Загружает JSON файл"""
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_csv(file: str) -> List[Dict]:
    """Загружает CSV файл"""
    with open(file, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def filter_by_status(transactions: List[Dict], status: str) -> List[Dict]:
    """Фильтрует по статусу"""
    return [t for t in transactions if t.get('status', '').upper() == status.upper()]


def sort_by_date(transactions: List[Dict], reverse: bool = False) -> List[Dict]:
    """Сортирует по дате"""
    return sorted(transactions, key=lambda x: x.get('date', ''), reverse=reverse)


def filter_rub(transactions: List[Dict]) -> List[Dict]:
    """Оставляет только рублевые транзакции"""
    return [t for t in transactions if t.get('currency', '').upper() == 'RUB']


def print_transactions(transactions: List[Dict]) -> None:
    """Выводит транзакции"""
    if not transactions:
        print("Нет подходящих транзакций")
        return

    print(f"Найдено операций: {len(transactions)}\n")
    for t in transactions:
        print(f"{t.get('date', 'Дата')} {t.get('description', 'Описание')}")
        if 'from' in t:
            print(f"{t['from']} -> {t.get('to', '')}")
        print(f"Сумма: {t.get('amount', '?')} {t.get('currency', '')}\n")


def main():
    print("Банковские транзакции\nВыберите тип файла:")
    print("1. JSON\n2. CSV")

    choice = input("Ваш выбор (1/2): ").strip()
    file = input("Путь к файлу: ").strip()

    try:
        transactions = load_json(file) if choice == '1' else load_csv(file)
    except Exception as e:
        print(f"Ошибка: {e}")
        return

    # Фильтр по статусу
    while True:
        status = input("Статус (EXECUTED/CANCELED/PENDING): ").upper()
        if status in ('EXECUTED', 'CANCELED', 'PENDING'):
            break
        print("Некорректный статус")

    transactions = filter_by_status(transactions, status)

    # Дополнительные фильтры
    if input("Сортировать по дате? (да/нет): ").lower() == 'да':
        reverse = input("По убыванию? (да/нет): ").lower() == 'да'
        transactions = sort_by_date(transactions, reverse)

    if input("Только рубли? (да/нет): ").lower() == 'да':
        transactions = filter_rub(transactions)

    if input("Фильтр по описанию? (да/нет): ").lower() == 'да':
        search = input("Слово для поиска: ")
        transactions = filter_by_description(transactions, search)

    print("\nРезультат:")
    print_transactions(transactions)


if __name__ == "__main__":
    main()