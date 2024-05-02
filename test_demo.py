import unittest
import demo


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.calculate = demo.Calculate()

    def tearDown(self):
        print("This is the tearDown method")

    def test_add(self):
        self.assertEqual(self.calculate.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(self.calculate.subtract(3, 2), 1)

    def test_multiply(self):
        self.assertEqual(self.calculate.multiply(3, 2), 6)

    def test_divide(self):
        self.assertEqual(self.calculate.divide(10, 2), 5)


if __name__ == '__main__':
    unittest.main()