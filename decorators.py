import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Засекаем время начала выполнения
        result = func(*args, **kwargs)  # Выполняем функцию
        end_time = time.time()  # Засекаем время окончания выполнения
        print(f"Функция {func.__name__} выполнялась {end_time - start_time} секунд.")
        return result
    return wrapper

@timing_decorator
def my_function():
    # Тут какая-то операция, время выполнения которой мы хотим измерить
    time.sleep(2)

decorated_function = timing_decorator(my_function())
