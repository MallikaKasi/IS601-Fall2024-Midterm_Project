"""Testing Addition """
import unittest
from unittest.mock import MagicMock
from app.commands import CommandHandler
from app.plugins.Add import AddCommand

class TestAddCommand(unittest.TestCase):
    """Testing """
    def setUp(self):
        """Set up the CommandHandler and AddCommand for each test."""
        self.command_handler = CommandHandler()
        self.command_handler.add_history = MagicMock()

    def test_addition(self):
        """Test that the AddCommand correctly adds two numbers."""
        add_command = AddCommand(5, 3, self.command_handler)
        add_command.execute()
        self.command_handler.add_history.assert_called_once_with('Add', 5, 3, 8)

if __name__ == '__main__':
    unittest.main()
