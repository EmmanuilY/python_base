"""
В Python, assert и raise используются для обработки исключений, но они используются по-разному.
assert используется для отладки и автоматического тестирования.
Он позволяет вам утверждать, что определенное условие истинно, и если это не так, то Python поднимает исключение AssertionError.
"""
print(1 == 1)  # Вывод: True
print('hello' == 'hello')  # Вывод: True
print([1, 2, 3] == [1, 2, 3])  # Вывод: True


a = [1, 2, 3]
b = a
print(a is b)  # Вывод: True
c = [1, 2, 3]
print(a is c)  # Вывод: False


with open('file.txt', 'r') as f:
    content = f.read()
# Здесь файл уже закрыт, даже если чтение вызвало исключение.
class MyContextManager:
    def __enter__(self):
        print("Входим в блок 'with'")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Выходим из блока 'with'")
        if exc_type is not None:
            print(f"Произошло исключение: {exc_val}")
        # return False  # Раскомментируйте, чтобы подавить исключение

with MyContextManager() as x:
    print("Внутри блока 'with'")
    # raise ValueError("Произошла ошибка!")  # Раскомментируйте, чтобы проверить обработку исключений
from functions import lru_cashe
@lru_cashe
def hi():
    pass

def cache_decorator(func):
    cache = dict()

    def cached_func(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return cached_func

# использование декоратора
@cache_decorator
def slow_function(a, b):
    # представим, что эта функция требует много времени для выполнения
    return a ** b

print(slow_function(2, 3))  # первый вызов, результат кешируется
print(slow_function(2, 3))