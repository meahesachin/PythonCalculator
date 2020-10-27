import math


def addition(a, b):
    c = float(a) + float(b)
    return float(c)


def subtraction(a, b):
    c = float(a)-float(b)
    return float(c)


def multiplication(a, b):
    c = float(a)*float(b)
    return float(c)


def division(a, b):
    c = float(a)/float(b)
    return float(c)


def squared(a):
    c = float(a) ** 2
    return c


def squareroot(a):
    c = math.sqrt(a)
    return float(c)


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        if float(b) < 1:
            return 0
        self.result = division(a, b)
        return format(self.result, '.9f')

    def square(self, a):
        self.result = squared(a)
        return self.result

    def sqrt(self, a):
        self.result = squareroot(int(a))
        if self.result.is_integer():
            return format(self.result, '.1f')
        else:
            return format(self.result, '.8f')



