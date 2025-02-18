from datetime import date
from typing import List, Union, Any, Optional

Number = Union[int, float]


def add(a: int | float, b: Union[int, float]) -> Number:
    return a + b


x: int = 10
print(x)

x = 'Hello'
print(x)

# res_1: int = add('hello', 8)
# res_2: str = add(8, 5)

res_3: Number = add(7, 2.44)

data: list[int] = [1, 8, 9]
nums: List[float] = [3.14, 2.71]
info: tuple[str, str, date] = ('Николай', 'Андреев', date(1998, 3, 10))

print(data[-1])
print(nums[0])
print(info)

greeting: Any = 'hello'
print(greeting)
greeting = 65
print(greeting)

y: Optional[int] = None
print(y)
y = 8
print(y)
