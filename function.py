"""
# Working on Function & Tuple Return
"""


def add(num1, num2=5):
    return num1 + num2


print(add(5, 2))
print(add(5))


def get_tuple_value():
    return 'apple', 'ball'


x, y = get_tuple_value()

print('x: ', x)
print('y: ', y)
