"""T"""
import unittest
from unittest.mock import patch, MagicMock
from app.plugins.ClearHistory import ClearHistoryCommand  # Import ClearHistoryCommand

class TestClearHistoryCommand(unittest.TestCase):
    """Tests for ClearHistoryCommand."""

    def setUp(self):
        """Set up a mock CommandHandler before each test."""
        self.mock_command_handler = MagicMock()

    @patch('logging.info')  # Patch the logging.info function to capture log messages
    def test_clear_history_empty(self, mock_logging):
        """Test clearing history when there is no history present."""
        # Create an instance of ClearHistoryCommand
        clear_history_command = ClearHistoryCommand(self.mock_command_handler)

        # Simulate no history by ensuring clear_history doesn't return anything
        self.mock_command_handler.clear_history.return_value = None

        # Call the execute method to clear history
        clear_history_command.execute()

        # Verify that clear_history was called on the command handler
        self.mock_command_handler.clear_history.assert_called_once()

        # Verify that logging was called with the correct message
        mock_logging.assert_called_with("Invoked Clear History Operation")

    @patch('logging.info')  # Patch the logging.info function to capture log messages
    def test_clear_history_with_existing_history(self, mock_logging):
        """Test clearing history when there is some history present."""
        # Create an instance of ClearHistoryCommand
        clear_history_command = ClearHistoryCommand(self.mock_command_handler)

        # Simulate some existing history
        self.mock_command_handler.history_df = MagicMock()

        # Call the execute method to clear history
        clear_history_command.execute()

        # Verify that clear_history was called on the command handler
        self.mock_command_handler.clear_history.assert_called_once()

        # Verify that logging was called with the correct message
        mock_logging.assert_called_with("Invoked Clear History Operation")

    @patch('logging.info')  # Patch the logging.info function to capture log messages
    def test_clear_history_logging(self, mock_logging):
        """Test that logging happens when clear history is invoked."""
        # Create an instance of ClearHistoryCommand
        clear_history_command = ClearHistoryCommand(self.mock_command_handler)

        # Call the execute method to clear history
        clear_history_command.execute()

        # Verify that logging was called with the correct message
        mock_logging.assert_called_with("Invoked Clear History Operation")

if __name__ == "__main__":
    unittest.main()
