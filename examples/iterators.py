from typing import Any, Iterable, Iterator


class Repeater(Iterable):
    value: Any
    count: int

    def __init__(self, value: Any, count: int) -> None:
        self.value = value
        self.count = count

    def __iter__(self) -> Iterator[Any]:
        return self

    def __next__(self) -> Any:
        if self.count == 0:
            raise StopIteration

        self.count -= 1
        return self.value


for element in Repeater(5, 2):
    print(element)

# # Вызываем __iter__ у объекта класса Repeater,
# # т.е. в нашем случае получаем сам объект
# it: Iterator = iter(Repeater(5))
# element: int = None
#
# while True:
#     try:
#         # Вызываем __next__ у итератора объекта класса Repeater
#         element = next(it)
#     except StopIteration:
#         break
#
#     print(element)
