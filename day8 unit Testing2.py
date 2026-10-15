import unittest

from password import is_valid_pass

class TestPassword(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(is_valid_pass('123456789'))

    def test_short_pass(self):
        self.assertFalse(is_valid_pass("abc"))



if __name__=="__main__":
    unittest.main()