def divide(x, y):
    return x / y


try:
    a = int(input())
    b = int(input())

    res = divide(a, b)
    print(res)
except (ZeroDivisionError, ArithmeticError) as e:
    print(e)
    print('Division by zero')
except ValueError as e:
    print(e)
    print('Non numeric input')
finally:
    print('Clean-up actions')

print('Hello?')
