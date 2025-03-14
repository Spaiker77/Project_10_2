import pytest
from src.decorators import log, my_function


@log()
def add(x, y):
    return x + y


@log()
def divide(x, y):
    return x / y


# Тест успешного выполнения функции
def test_add(capsys):
    result = add(3, 4)
    assert result == 7

    # Перехват вывода в консоль
    captured = capsys.readouterr()
    assert "Starting add with args: (3, 4), kwargs: {}" in captured.out
    assert "add ok" in captured.out


# Тест обработки исключения
def test_divide_by_zero(capsys):
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    # Перехват вывода в консоль
    captured = capsys.readouterr()
    assert "Starting divide with args: (1, 0), kwargs: {}" in captured.out
    assert "divide error: ZeroDivisionError. Inputs: (1, 0), kwargs: {}" in captured.out


# Тест с неправильными типами
def test_add_with_invalid_type(capsys):
    with pytest.raises(TypeError):
        add(1, 'a')

    # Перехват вывода в консоль
    captured = capsys.readouterr()
    assert "Starting add with args: (1, 'a'), kwargs: {}" in captured.out
    assert "add error: TypeError. Inputs: (1, 'a'), kwargs: {}" in captured.out

