from functools import reduce


class SimpleCalculator:
    def add(self, *args):
        return sum(args)

    def subtract(self, a, b):
        return a - b

    def multiply(self, *args):
        def mul(x, y):
            return x * y
        return reduce(lambda x, y: x * y, args)
