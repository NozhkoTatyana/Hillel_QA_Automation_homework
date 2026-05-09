def log_decorator(func):
    """
    декоратор, який логує аргументи та результати викликаної функції.
    """
    def wrapper(*args, **kwargs):
        print(f"Виклик {func.__name__} з аргументами {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper


def exception_handler(func):
    """
    декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Помилка: {e}")
            return None
    return wrapper


@log_decorator
def add(a, b):
    return a + b

@exception_handler
def divide(a, b):
    return a / b



if __name__ == "__main__":
    add(2, 3)
    add(a=2, b=3)
    divide(10, 0)
