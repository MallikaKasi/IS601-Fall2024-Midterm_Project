""" TEST Main File """
from decimal import Decimal
from unittest.mock import patch, MagicMock

import pytest
#from app.calculator import Calculator
from main import OperationCommand, main,calculate_and_print

# Parameterize the test function to cover different operations and scenarios, including errors
@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "0", 'divide', "Unable to divide by 0"),  # Adjusted for the actual error message
    ("9", "3", 'unknown', "Unknown operation: unknown"),  # Test for unknown operation
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),  # Testing invalid number input
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")  # Testing another invalid number input
])
def test_calculate_and_print(a_string, b_string, operation_string,expected_string, capsys):
    """ TEST test_calculate_and_print Function """
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string

# Mock Calculator methods to simplify testing
class MockCalculator:
    """ TEST test_calculate_and_print Function """

    @staticmethod
    def Add(a, b):
        """ TEST test_calculate_and_print Function """
        return a + b

    @staticmethod
    def Subtract(a, b):
        """ TEST test_calculate_and_print Function """
        return a - b

    @staticmethod
    def Multiply(a, b):
        """ TEST test_calculate_and_print Function """
        return a * b

    @staticmethod
    def Divide(a, b):
        """ TEST test_calculate_and_print Function """
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b

def test_unknown_operation():
    '''Test the handling of an unknown operation'''
    command = OperationCommand(MockCalculator, 'UnknownOp', Decimal('10'), Decimal('5'))
    with pytest.raises(ValueError, match="Unknown operation: UnknownOp"):
        command.execute()

def test_divide_by_zero():
    '''Test the handling of division by zero'''
    command = OperationCommand(MockCalculator, 'Divide', Decimal('10'), Decimal('0'))
    with pytest.raises(ZeroDivisionError, match="Division by zero"):
        command.execute()

# Mock sys.argv to test the main function behavior
@patch('sys.argv', ['main.py', 'I'])
@patch('main.App')
def test_main_interactive_mode(mock_app_class):
    """Test the interactive mode when 'I' is passed as an argument."""
    mock_app_instance = MagicMock()
    mock_app_class.return_value = mock_app_instance

    main()

    # Check if App's start method was called
    mock_app_instance.start.assert_called_once()

@patch('sys.argv', ['main.py', '10', '5', 'add'])
def test_main_command_line_calculation(capsys):
    """Test the command-line calculation mode."""
    main()
    captured = capsys.readouterr()
    assert "The result of 10 add 5 is equal to 15" in captured.out

@patch('sys.argv', ['main.py'])
def test_main_help_message(capsys):
    """Test that the help message is displayed with incorrect arguments."""
    with pytest.raises(SystemExit):  # Expecting sys.exit to be called
        main()
    captured = capsys.readouterr()
    assert "Incorrect Number of arguments , So Exiting the Application" in captured.out
    #assert "Usage of this Calculator Application:" in captured.out
