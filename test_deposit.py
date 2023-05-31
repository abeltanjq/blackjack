import unittest
from unittest.mock import patch
from blackjack import input_deposit

class InputDepositTestCase(unittest.TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_input_deposit_valid_integer(self, mock_input):
        expected_result = 1.0
        deposit = input_deposit()
        self.assertEqual(deposit, expected_result)

if __name__ == '__main__':
    unittest.main()
