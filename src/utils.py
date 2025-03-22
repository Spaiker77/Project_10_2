import json
import os
from typing import List, Dict, Any


def read_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает транзакции из JSON-файла и возвращает их в виде списка словарей.
    Если файл не найден, пустой или содержит не список, возвращает пустой список.

    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data: Any = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, UnicodeDecodeError):
        return []

if __name__ == '__main__':
    print(read_transactions('../data/operations.json'))