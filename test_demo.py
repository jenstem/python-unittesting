import unittest
import demo


class TestDemo(unittest.TestCase):

    def test_add(self):
        calculate = demo.Calculate()
        self.assertEqual(calculate.add(1, 2), 3)

    def test_subtract(self):
        calculate = demo.Calculate()
        self.assertEqual(calculate.subtract(3, 2), 1)

    def test_multiply(self):
        calculate = demo.Calculate()
        self.assertEqual(calculate.multiply(3, 2), 6)

    def test_divide(self):
        calculate = demo.Calculate()
        self.assertEqual(calculate.divide(10, 2), 5)


if __name__ == '__main__':
    unittest.main()