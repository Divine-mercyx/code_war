import unittest
import palindrome

class TestPalindrome(unittest.TestCase):

    def test_if_number_is_palindrome(self):
        actual = palindrome.is_palindrome(121)
        expected = True
        self.assertEqual(actual, expected)
