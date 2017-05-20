# Working on Class


class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y


calc = Calculator(10, 2)

print(calc.add())
print(calc.subtract())
print(calc.multiply())
print(calc.divide())
