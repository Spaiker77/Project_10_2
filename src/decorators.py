def log(filename=None):
    """
    Декоратор, который будет автоматически логировать начало и конец
    выполнения функции, а также ее результаты или возникшие ошибки.

    filename: Имя файла для записи логов. Если None, выводит в консоль.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            log_message = f"Starting {func.__name__} with args: {args}, kwargs: {kwargs}"
            write_log(log_message, filename)
            try:
                result = func(*args, **kwargs)
                success_message = f"{func.__name__} ok"
                write_log(success_message, filename)
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, kwargs: {kwargs}"
                write_log(error_message, filename)
                raise

        # Сохраняем имя функции и её документацию
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper

    return decorator


def write_log(message, filename):
    if filename:
        with open(filename, "a") as log_file:
            log_file.write(message + "\n")
    else:
        print(message)


# Пример использования
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y
