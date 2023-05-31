# Deposit
Using `isdigit` does not check if the value is a float. It has to be all digits.

When using `@patch` decorator, the `@patch` closest to the test fuction will have the parameter listed first.

```py
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['notnumber'])
    def test_prompt_user_to_input_a_number(self, mock_input, mock_stdout)
        ...
```