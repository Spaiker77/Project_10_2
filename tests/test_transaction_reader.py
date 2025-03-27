from unittest.mock import patch, MagicMock
from src.transaction_reader import read_csv_transactions, read_excel_transactions

# Пути к файлам
CSV_PATH = r"C:\Users\spaik\PycharmProjects\pythonProject1\src\transactions.csv"
EXCEL_PATH = r"C:\Users\spaik\PycharmProjects\pythonProject1\src\transactions_excel.xlsx"


def test_read_csv_success():
    """Тест чтения CSV"""
    mock_data = MagicMock()
    mock_data.to_dict.return_value = [{"Дата": "2023-01-01", "Сумма": 100, "Описание": "Покупка"}]

    with patch("os.path.exists", return_value=True), patch("pandas.read_csv", return_value=mock_data):
        result = read_csv_transactions()
        assert isinstance(result, list)
        assert len(result) > 0  # Простая проверка, что данные есть


def test_read_excel_success():
    """Тест чтения Excel"""
    mock_data = MagicMock()
    mock_data.to_dict.return_value = [{"Дата": "2023-01-01", "Сумма": 150, "Описание": "Оплата"}]

    with patch("os.path.exists", return_value=True), patch("pandas.read_excel", return_value=mock_data):
        result = read_excel_transactions()
        assert isinstance(result, list)
        assert len(result) > 0


def test_file_not_found():
    """Тест отсутствия файлов"""
    with patch("os.path.exists", return_value=False):
        assert read_csv_transactions() == []
        assert read_excel_transactions() == []


def test_read_errors():
    """Тест ошибок чтения"""
    with patch("os.path.exists", return_value=True):
        with patch("pandas.read_csv", side_effect=Exception("CSV Error")):
            assert read_csv_transactions() == []

        with patch("pandas.read_excel", side_effect=Exception("Excel Error")):
            assert read_excel_transactions() == []
