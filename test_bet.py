import unittest
from unittest.mock import patch
from blackjack import input_bet

class InputBetTestCase(unittest.TestCase):
    @patch('builtins.input', side_effect=['10'])
    def test_returns_input_bet_amount(self, mock_input):
        self.assertEqual(10, input_bet(15))

    @patch('builtins.input', side_effect=['10'])
    def test_bet_more_than_zero_but_less_than_deposit(self, mock_input):
        self.assertEqual(10, input_bet(15))

    @patch('builtins.input', side_effect=['15', '8'])
    def test_invalid_input_is_not_accepted_until_a_valid_one_is_given(self, mock_input):
        self.assertEqual(8, input_bet(10))
    
    @patch('builtins.input', side_effect=['nondigit', '8'])
    def test_non_digit_is_not_accepted_until_a_valid_one_is_given(self, mock_input):
        self.assertEqual(8, input_bet(10))

if __name__ == '__main__':
    unittest.main()
