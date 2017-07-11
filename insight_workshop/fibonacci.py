# Fibonacci Series


number = int(input("Input Number: "))
a = 0
b = 1

while a < number:
    print(a)
    a, b = b, a + b
