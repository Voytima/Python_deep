from collections import deque
import unittest


class TestFactorial(unittest.TestCase):

    def setUp(self) -> None:
        self.f = Factorial(3)
        self.f(1)
        self.f(3)
        self.f(2)
        self.f.printer()

        self.f1 = Factorial(2)
        self.f1(2)
        self.f1(3)
        self.f1(1)
        self.f1.printer()

    def test_calculation_1(self):
        self.assertEqual(self.f(1), 1)

    def test_calculation_2(self):
        self.assertEqual(self.f(3), 6)

    def test_calculation_3(self):
        self.assertEqual(self.f(2), 2)

    def test_printer_1(self):
        self.assertEqual(self.f.printer(), deque([{1: 1}, {3: 6}, {2: 2}], maxlen=3))

    def test_printer_2(self):
        self.assertEqual(self.f1.printer(), deque([{3: 6}, {1: 1}], maxlen=2))


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
    unittest.main(verbosity=2)
