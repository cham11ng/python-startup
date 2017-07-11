# Python For Calculating
# Greatest Common Divisor


def gcd(number1: int, number2: int) -> int:
    while number2:
        number1, number2 = number2, number1 % number2

    return number1


a = int(input('Number 1: '))
b = int(input('Number 2: '))

print(gcd(a, b))
