import unittest
from unittest.mock import patch
from blackjack import input_deposit

class InputDepositTestCase(unittest.TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_input_deposit_valid_integer(self, mock_input):
        expected_result = 1
        deposit = input_deposit()
        self.assertEqual(deposit, expected_result)

    @patch('builtins.input', side_effect=['notnumber', '2'])
    def test_accepts_valid_input_after_invalid_input(self, mock_input):
        expected_result = 2
        deposit = input_deposit()
        self.assertEqual(deposit, expected_result)
    
    @patch('builtins.input', side_effect=['0.5', '1'])
    def test_accepts_valid_input_after_rejecting_number_less_than_1(self, mock_input):
        expected_result = 1
        deposit = input_deposit() 
        self.assertEqual(deposit, expected_result)

if __name__ == '__main__':
    unittest.main()
