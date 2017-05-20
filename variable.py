# Global and Local Variable

x = 6


def addition(y):
    global x
    print('x = ', x)
    print('y = ', y)
    x += y
    print('Doing (x = x + y)')
    print('x = ', x)


addition(5)
