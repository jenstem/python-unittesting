import unittest
import demo


class TestDemo(unittest.TestCase):
    def test_demo(self):
        calculate = demo.Calculate()
        self.assertEqual(calculate.add(1, 2), 3)



if __name__ == '__main__':
    unittest.main()