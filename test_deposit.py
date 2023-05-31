import unittest
from unittest.mock import patch
from io import StringIO
from blackjack import input_deposit

class InputDepositTestCase(unittest.TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_input_deposit_valid_integer(self, mock_input):
        expected_result = 1.0
        deposit = input_deposit()
        self.assertEqual(deposit, expected_result)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['notnumber'])
    def test_prompt_user_to_input_a_number(self, mock_input, mock_stdout):
        input_deposit()
        expected_output = "Deposit has to be a number >= 1.\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
