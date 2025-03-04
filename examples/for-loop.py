from typing import Iterator

data: list[int] = [1, 3, 6, 10, 15, 21]
data: set[int] = set(data)

# for element in data:
#     print(element)

it: Iterator = iter(data)
element: int = None

while True:
    try:
        element = next(it)
    except StopIteration:
        break

    print(element)
