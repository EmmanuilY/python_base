def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# классический пример рекурсии

f = lambda x: x * 2
print(f(2))  # Выводит: 4

from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Выводит: 120

"""
reduce используется для применения функции к двум элементам последовательности, 
затем к результату и следующему элементу, 
и так далее, чтобы в конечном итоге "сократить" последовательность до одного значения. 
"""

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = zip(names, ages)
print(list(combined))  # Выводит: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
"""
В результате получается итератор, который возвращает кортежи, где i-й кортеж содержит i-й элемент из каждой входной коллекции.
"""

names = ["Alice", "Bob", "Charlie"]
for i, name in enumerate(names):
    print(f"Person {i} is named {name}")

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]
sums = map(lambda x, y: x + y, numbers1, numbers2)
print(list(sums))  # Выводит: [7, 9, 11, 13, 15]

"""

Функция map в Python возвращает специальный объект типа map, который является итератором. 
Это означает, что вычисления функции map, которую вы передаете в качестве первого аргумента, происходят "лениво".
Это значит, что вычисления происходят только тогда, когда вы итерируетесь по элементам итератора.
Функция map() в Python принимает минимум два аргумента:

Функцию, которую нужно применить к каждому элементу.
Один или более итерируемых объектов, к которым применяется функция.
"""


def print_best():
    best = 0

    def print_best():
        nonlocal best
        best += 10  # без nonlocal нельзя изменить best
        print(best)  # 10

    print_best()


print_best()


def make(N):
    def action(X):
        return X ** N

    return action


f = make(2)  # передаем аргумент в N
print(f(3))  # 9


def tester(start):
    def nested(label):
        print(label, state[0])  # Использует в своих интересах изменение
        # на месте изменяемого объекта
        state[0] += 1  # Добавочный синтаксис, глубинная магия?

    state = [start]
    return nested


print(tester(10)) # <function tester.<locals>.nested at 0x0000020C8803D360>



def action(x):
    return (lambda y: x + y)

act =action(12)
print(act) # <function action.<locals>.<lambda> at 0x0000020C8803D3F0>
print(act(10)) # 22
