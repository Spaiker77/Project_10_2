import json
import logging
import os
from typing import Any, Dict, List

# Настройка логгера
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)


# Настройка обработчика файла
file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_handler.setLevel(logging.DEBUG)

# Настройка форматера
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)


def read_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает транзакции из JSON-файла и возвращает их в виде списка словарей.
    Если файл не найден, пустой или содержит не список, возвращает пустой список.
    """
    try:
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            return []

        with open(file_path, "r", encoding="utf-8") as file:
            data: Any = json.load(file)

            if not isinstance(data, list):
                logger.error(f"File {file_path} does not contain a list of transactions")
                return []

            logger.debug(f"Successfully read {len(data)} transactions from {file_path}")
            return data

    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        logger.error(f"Error decoding file {file_path}: {str(e)}")
        return []
    except Exception as e:
        logger.error(f"Unexpected error reading file {file_path}: {str(e)}")
        return []


if __name__ == "__main__":
    print(read_transactions("../data/operations.json"))
