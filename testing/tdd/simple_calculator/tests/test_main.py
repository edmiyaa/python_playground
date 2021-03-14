from simple_calculator.main import SimpleCalculator


def test_add_two_numbers():
    calculator = SimpleCalculator()
    result = calculator.add(4, 5)
    assert result == 9

def test_add_three_numbers():
    calculator = SimpleCalculator()
    result = calculator.add(4, 5, 6)
    assert result == 15

def test_add_many_numbers():
    calculator = SimpleCalculator()
    numbers = range(100)
    result = calculator.add(*numbers)
    assert result == 4950

def test_subtract_two_numbers():
    calculator = SimpleCalculator()
    result = calculator.subtract(10, 3)
    assert result == 7

def test_multiply_two_numbers():
    calculator = SimpleCalculator()
    result = calculator.multiply(6, 4)
    assert result == 24

def test_multiply_five_numbers():
    calculator = SimpleCalculator()
    result = calculator.multiply(2, 6, 4, 8 ,3)
    assert result == 1152

def test_multiply_many_numbers():
    calculator = SimpleCalculator()
    numbers = range(1, 10)
    result = calculator.multiply(*numbers)
    assert result == 362880
