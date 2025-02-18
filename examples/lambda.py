from typing import Callable, Any


def add(a: int, b: int) -> int:
    return a + b


def transform(func: Callable, values: list[Any]) -> list[Any]:
    result = []
    for x in values:
        result.append(func(x))
    return result


def add_const(c: int) -> Callable:
    return lambda x: x + c


def multiply_const(c: int) -> Callable:
    def multiply(x: int) -> int:
        return x * c

    return multiply


print(add(1, 2))

another_add = add
print(another_add(1, 2))

del add

# print(add(1, 2))
print(another_add(3, 7))

data = [7, 8, 9, 1, -2, -7, 6]
print(*map(lambda x: x ** 2, data))
print(*transform(lambda x: x ** 2, data))

data.sort(key=lambda x: abs(x))
print(*data)

add_5 = add_const(5)
print(add_5(8))

multiply_5 = multiply_const(5)
print(multiply_5(8))
