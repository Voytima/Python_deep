from collections import deque
import pytest


@pytest.fixture
def memory_test_1():
    f = Factorial(3)
    f(1)
    f(3)
    f(2)
    memory_1 = f.printer()
    return memory_1


@pytest.fixture
def memory_test_2():
    f = Factorial(2)
    f(2)
    f(3)
    f(1)
    memory_2 = f.printer()
    return memory_2


def test_calculation_1():
    f = Factorial(3)
    assert f(1) == 1


def test_calculation_2():
    f = Factorial(3)
    assert f(3) == 6


def test_calculation_3():
    f = Factorial(2)
    assert f(2) == 2


def test_printer_1(memory_test_1):
    assert memory_test_1 == deque([{1: 1}, {3: 6}, {2: 2}], maxlen=3)


def test_printer_2(memory_test_2):
    assert memory_test_2 == deque([{3: 6}, {1: 1}], maxlen=2)


class Factorial:

    def __init__(self, k: int):
        self.memory = deque(maxlen=k)

    def __call__(self, n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        self.memory.append({n: result})
        return result

    def printer(self):
        return self.memory


if __name__ == '__main__':
    pytest.main(['-vv'])
