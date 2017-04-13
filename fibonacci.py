# fibonacci series


def fibonacci(x):
    sequence_list = []

    current = 0
    another = 1

    for i in range(x):
        sequence_list.append(current)
        current = another
        if i > 0:
            another = sequence_list[i] + current
        else:
            another = 1
    return sequence_list


# produces a sum for the kth fibonacci number
def print_fibonacci(x):
    print(str(fibonacci(x)))

length = int(input('Length of Fibonacci Series: '))

print_fibonacci(length)
