# prime number

prime_number_list = []

length = int(input('Prime Number Limit: '))

for i in range(2, length):
    for j in range(2, i):
        if i % j == 0:
            print(i, " equals ", j, 'x', i // j)
            break
    # it is executed when the loop terminates through exhaustion of the list
    # (with for) or
    else:
        # when the condition becomes false (with while)
        print(i, " is a prime number")
        prime_number_list.append(i)

print(prime_number_list)
