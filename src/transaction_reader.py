import pandas as pd
import os


def read_csv_transactions():
    """Чтение транзакций из CSV файла"""
    file_path = os.path.join(os.path.dirname(__file__), "transactions.csv")

    if not os.path.exists(file_path):
        print(f"CSV файл не найден: {file_path}")
        return []

    try:
        data = pd.read_csv(file_path).to_dict("records")
        print(f"Прочитано {len(data)} записей CSV")
        return data
    except Exception as e:
        print(f"Ошибка чтения CSV: {e}")
        return []


def read_excel_transactions():
    """Чтение транзакций из Excel файла"""
    file_path = os.path.join(os.path.dirname(__file__), "transactions_excel.xlsx")

    if not os.path.exists(file_path):
        print(f"Excel файл не найден: {file_path}")
        return []

    try:
        data = pd.read_excel(file_path).to_dict("records")
        print(f"Прочитано {len(data)} записей из Excel")
        return data
    except Exception as e:
        print(f"Ошибка чтения Excel: {e}")
        return []


if __name__ == "__main__":
    print("Загрузка")

    csv_data = read_csv_transactions()
    excel_data = read_excel_transactions()

    if csv_data:
        print("\nДанные CSV:", csv_data[0])
    if excel_data:
        print("Данные Excel:", excel_data[0])

    print("\nГотово!")
