"""TESTING"""
import unittest
from unittest.mock import patch, MagicMock
from app.plugins.History import HistoryCommand, register
from app.commands import CommandHandler

class TestHistoryCommand(unittest.TestCase):
    """TESTING"""
    def setUp(self):
        """Setup a mock CommandHandler before each test."""
        # Create a mock CommandHandler
        self.mock_command_handler = MagicMock(spec=CommandHandler)

    @patch('builtins.print')  # Mock the print function to capture output
    @patch('logging.info')  # Mock logging to avoid cluttering the test output
    def test_execute_no_history(self, mock_logging, mock_print):
        """Test the execute method when there is no history."""
        # Simulate get_history returning no history
        self.mock_command_handler.get_history.return_value = "No calculations are available. Please enter a command."

        # Create an instance of HistoryCommand
        history_command = HistoryCommand(self.mock_command_handler)

        # Call execute method
        history_command.execute()

        # Ensure logging is called with the correct message
        mock_logging.assert_called_with("Invoked History Operation")

        # Ensure it prints the message when no history is available
        mock_print.assert_called_with("No calculations are available. Please enter a command.")

    @patch('builtins.print')  # Mock the print function to capture output
    @patch('logging.info')  # Mock logging to avoid cluttering the test output
    def test_execute_with_history(self, mock_logging, mock_print):
        """Test the execute method when there is history."""
        # Simulate get_history returning history data
        self.mock_command_handler.get_history.return_value = "History: Add 1 + 1 = 2"

        # Create an instance of HistoryCommand
        history_command = HistoryCommand(self.mock_command_handler)

        # Call execute method
        history_command.execute()

        # Ensure logging is called with the correct message
        mock_logging.assert_called_with("Invoked History Operation")

        # Ensure it prints the correct history
        mock_print.assert_called_with("History: Add 1 + 1 = 2")

    def test_register_function(self):
        """Test that the register function returns a HistoryCommand instance."""
        # Call the register function with the mock CommandHandler
        result = register(self.mock_command_handler)

        # Ensure the result is an instance of HistoryCommand
        self.assertIsInstance(result, HistoryCommand)

        # Ensure the command handler is correctly passed to the HistoryCommand
        self.assertEqual(result.command_handler, self.mock_command_handler)

if __name__ == '__main__':
    unittest.main()
