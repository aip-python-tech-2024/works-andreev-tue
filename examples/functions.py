import traceback


def square(x):
    # traceback.print_stack()
    return x ** 2


def add(a, b, *args, **kwargs):
    print(args)
    print(kwargs)

    s = a + b

    for x in args:
        s += x

    for key in kwargs:
        s += kwargs[key]

    return s


def f(x):
    return add(square(x), 2*x, 6)


print('Hello World!')

res = add(7, 3, 4)
print(res)

another_res = add(10, 7)
print(another_res)

print(f(7) + square(7))

print(add(7, 6, 1, 4, 8, 10, -2, 0))
print(add(7, 6, x=8))

data = [7, 5, 6, 1, 0]
config = {'sep': ', ', 'end': '!\n'}
print(add(*data))
print(*data, **config)
