import unittest

from calculator import add,sub,mul,div,even,odd

class TestAddition(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5,3),8)

    def test_sub(self):
        self.assertEqual(sub(10,5),5)

    def test_mul(self):
        self.assertEqual(mul(2,4),8)

    def test_div(self):
        self.assertEqual(div(4,2),2)

    def test_even(self):
        self.assertEqual(even(4),'even')

    def test_odd(self):
        self.assertEqual(odd(3),'odd')


if __name__=="__main__":
    unittest.main()