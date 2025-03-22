from unittest.mock import mock_open, patch
import src.utils

@patch("os.path.exists")
def test_read_transactions_file_not_found(mock_exists) -> None:
    mock_exists.return_value = False
    assert src.utils.read_transactions("invalid_path.json") == []

@patch("os.path.exists")
def test_read_transactions_invalid_json(mock_exists) -> None:
    mock_exists.return_value = True
    with patch("builtins.open", mock_open(read_data="invalid json")):
        assert src.utils.read_transactions("dummy.json") == []

@patch("os.path.exists")
def test_read_transactions_valid_list(mock_exists) -> None:
    mock_exists.return_value = True
    data = '[{"id": 1}, {"id": 2}]'
    with patch("builtins.open", mock_open(read_data=data)):
        assert src.utils.read_transactions("valid.json") == [{"id": 1}, {"id": 2}]

@patch("os.path.exists")
def test_read_transactions_not_a_list(mock_exists) -> None:
    mock_exists.return_value = True
    data = '{"id": 1}'
    with patch("builtins.open", mock_open(read_data=data)):
        assert src.utils.read_transactions("not_list.json") == []