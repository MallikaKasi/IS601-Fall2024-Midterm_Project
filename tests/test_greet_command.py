"""Testing"""
import unittest
from unittest.mock import patch
from app.plugins.Greet import GreetCommand, register  # Import GreetCommand

class TestGreetCommand(unittest.TestCase):
    """Unit tests for GreetCommand."""

    def setUp(self):
        """Set up a GreetCommand instance."""
        self.greet_command_instance = register()  # Ensure this returns an instance of GreetCommand

    @patch('builtins.print')  # Mock the print function
    @patch('logging.info')  # Mock the logging function
    def test_greet_message(self, mock_logging, mock_print):
        """Test if GreetCommand prints, logs, and returns the correct greeting message."""
        greet_command = self.greet_command_instance  # This is now an instance

        # Execute the command and check the result
        result = greet_command.execute()
        expected_message = "Hello! Welcome to the Interactive Calculator."

        # Assert the result is the expected message
        self.assertEqual(result, expected_message, "Greeting message should match.")

        # Ensure the message was printed
        mock_print.assert_called_once_with(expected_message)

        # Ensure the message was logged correctly
        mock_logging.assert_any_call("Invoked Greet Operation")
        mock_logging.assert_any_call(expected_message)

    @patch('builtins.print')  # Mock the print function
    def test_greet_message_repeated_execution(self, mock_print):
        """Test executing the GreetCommand multiple times."""
        greet_command = self.greet_command_instance  # This is now an instance

        # Execute the command multiple times
        for _ in range(3):
            result = greet_command.execute()
            expected_message = "Hello! Welcome to the Interactive Calculator."

            # Assert the result is correct each time
            self.assertEqual(result, expected_message, "Greeting message should match each time.")

            # Ensure the message is printed each time
            mock_print.assert_called_with(expected_message)

    @patch('logging.info')  # Mock the logging function
    def test_logging(self, mock_logging):
        """Test that logging happens correctly during GreetCommand execution."""
        greet_command = self.greet_command_instance  # This is now an instance

        # Execute the command
        greet_command.execute()

        # Ensure logging was called with the correct messages
        mock_logging.assert_any_call("Invoked Greet Operation")
        mock_logging.assert_any_call("Hello! Welcome to the Interactive Calculator.")

    def test_register_returns_greet_command(self):
        """Test that the register function returns an instance of GreetCommand."""
        # Ensure the registered command is an instance of GreetCommand
        greet_command = self.greet_command_instance
        self.assertIsInstance(greet_command, GreetCommand, "GreetCommand should be returned by register.")

if __name__ == "__main__":
    unittest.main()
