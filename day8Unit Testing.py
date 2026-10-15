import unittest

from calculator import add,sub,mul

class TestAddition(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5,3),8)

    def test_sub(self):
        self.assertEqual(sub(10,5),5)

    def test_mul(self):
        self.assertEqual(mul(2,4),8)


if __name__=="__main__":
    unittest.main()