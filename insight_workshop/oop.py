# Object Oriented


class Number:
    price = 1

    def __init__(self, price):
        self.price = price

    def check_odd_even(self):
        if self.price % 2:
            return str(self.price) + " is Odd Number"
        else:
            return str(self.price) + " is Even Number"


number = int(input("Enter a Number: "))
numObject = Number(number)

print(numObject.check_odd_even())
