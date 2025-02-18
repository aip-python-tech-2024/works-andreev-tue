from typing import Callable


def log(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print("Function has been called")
        return func(*args, **kwargs)

    return wrapper


@log
def greet():
    print("Hello, world!")


@log
def add(a: int, b: int) -> int:
    return a + b


# greet = log(greet)
greet()
print(add(1, 2))
