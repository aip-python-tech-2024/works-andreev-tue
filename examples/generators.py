from typing import Generator


def add(a, b) -> Generator:
    yield a + b
    yield a + a + b + b


def repeater(value, count) -> Generator:
    while count != 0:
        yield value
        count -= 1


def get_fibonacci() -> Generator:
    a, b = 0, 1
    while True:
        yield a
        if a > 100:
            return
        a, b = b, a + b


def another_add(a, b) -> Generator:
    yield from add(a, b)


for x in another_add(1, 2):
    print(x)

for x in repeater(5, 3):
    print(x)

for i, x in enumerate(filter(lambda t: t % 2 == 0, get_fibonacci())):
    print(i, x)
    if i == 50:
        break
