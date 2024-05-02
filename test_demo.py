import unittest
import demo


class TestDemo(unittest.TestCase):
    def test_add(self):
        self.assertEqual(demo.add(2, 2), 4)
        self.assertEqual(demo.add(10, 4), 14)
        self.assertEqual(demo.add(23, 7), 30)


if __name__ == '__main__':
    unittest.main()