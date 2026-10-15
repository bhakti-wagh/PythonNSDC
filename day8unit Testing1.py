import unittest

from calculator import even,odd,is_prime

class Number_Check(unittest.TestCase):

   

    def test_even(self):
        self.assertTrue(even(4),'even')


    def test_odd(self):
        self.assertTrue(odd(3),'odd')

    
    def test_prime(self):
        self.assertTrue(is_prime(2),True)


if __name__=="__main__":
    unittest.main()