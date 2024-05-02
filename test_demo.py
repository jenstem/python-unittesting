import unittest
import demo


class TestDemo(unittest.TestCase):

    def test_add(self):
        self.assertEqual(demo.add(2, 2), 4)
        self.assertEqual(demo.add(10, 4), 14)
        self.assertEqual(demo.add(23, 7), 30)

    def test_sub(self):
        self.assertEqual(demo.sub(4, 2), 2)
        self.assertEqual(demo.sub(10, 4), 6)
        self.assertEqual(demo.sub(23, 7), 16)

    def test_multiple(self):
        self.assertEqual(demo.multiple(2, 2), 4)
        self.assertEqual(demo.multiple(10, 4), 40)
        self.assertEqual(demo.multiple(20, 5), 100)

    def test_divide(self):
        self.assertEqual(demo.divide(4, 2), 2)
        self.assertEqual(demo.divide(10, 2), 5)
        self.assertEqual(demo.divide(21, 7), 3)


if __name__ == '__main__':
    unittest.main()