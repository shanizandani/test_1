import unittest
from app import perform_operation
from func_enum import Operation



# Define a test class for the 'perform_operation' function
class TestPerformOperation(unittest.TestCase):
    # Test the 'perform_operation' function with addition
    def test_addition(self):
        self.assertEqual(perform_operation(2, 3, Operation.ADD), 5)
    # Test the 'perform_operation' function with subtraction
    def test_subtraction(self):
        self.assertEqual(perform_operation(5, 1, Operation.SUBTRACT), 4)
    # Test the 'perform_operation' function with sum of digits
    def test_sum_of_digits(self):
        self.assertEqual(perform_operation(123, None, Operation.SUM_OF_DIGITS), 6)
    # Test the 'perform_operation' function with palindrome check
    def test_is_palindrome(self):
        self.assertTrue(perform_operation(121, None, Operation.IS_PALINDROME))
    # Test the 'perform_operation' function with zip
    def test_my_zip(self):
        self.assertEqual(list(perform_operation([1, 2, 3], ['a', 'b', 'c'], Operation.MY_ZIP)), [(1, 'a'), (2, 'b'), (3, 'c')])



# Run all the tests defined in the test classes
if __name__ == '__main__':
    unittest.main()
