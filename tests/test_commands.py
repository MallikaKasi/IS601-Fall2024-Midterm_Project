"""T"""
import unittest
import os
from unittest.mock import MagicMock, patch
from app.commands import CommandHandler, Command

class TestCommandHandler(unittest.TestCase):
    """Tests for CommandHandler class."""

    def setUp(self):
        """Set up a CommandHandler instance for each test."""
        self.command_handler = CommandHandler()

    def test_register_command(self):
        """Test that a command can be registered."""
        mock_command = MagicMock(spec=Command)
        self.command_handler.register_command('TestCommand', mock_command)

        # Ensure that the command is stored in the commands dictionary
        self.assertIn('TestCommand', self.command_handler.commands)
        self.assertEqual(self.command_handler.commands['TestCommand'], mock_command)

    def test_execute_command_valid(self):
        """Test that a valid command is executed correctly."""
        mock_command = MagicMock()
        self.command_handler.register_command('TestCommand', mock_command)

        self.command_handler.execute_command('TestCommand')

        # Ensure that the command's execute method was called
        mock_command.execute.assert_called_once()

    def test_execute_command_invalid(self):
        """Test that an invalid command logs an error."""
        with patch('logging.info') as mock_logging:
            self.command_handler.execute_command('InvalidCommand')

            # Ensure logging is called for the invalid command
            mock_logging.assert_called_with("No such command: InvalidCommand")

    def test_add_history(self):
        """Test adding a history record to the DataFrame."""
        # Add a history record
        self.command_handler.add_history('Add', 5, 10, 15)

        # Ensure the history DataFrame is updated
        self.assertEqual(len(self.command_handler.history_df), 1)

        expected_history = {
            'Operation': 'Add',
            'Value1': 5.0,
            'Value2': 10.0,
            'Result': 15.0
        }
        record = self.command_handler.history_df.iloc[0].to_dict()
        self.assertEqual(record, expected_history)

    def test_clear_history(self):
        """Test clearing the history."""
        # Add a history record
        self.command_handler.add_history('Add', 5, 10, 15)

        # Clear the history
        self.command_handler.clear_history()

        # Ensure the DataFrame is empty after clearing
        self.assertTrue(self.command_handler.history_df.empty)

    def test_delete_calculation_by_index(self):
        """Test deleting a history record by index."""
        # Add two history records
        self.command_handler.add_history('Add', 5, 10, 15)
        self.command_handler.add_history('Subtract', 20, 5, 15)

        # Delete the first record (index 0)
        self.command_handler.delete_calculation_by_index(0)

        # Ensure that only one record remains
        self.assertEqual(len(self.command_handler.history_df), 1)
        self.assertEqual(self.command_handler.history_df.iloc[0]['Operation'], 'Subtract')

    def test_delete_calculation_invalid_index(self):
        """Test deleting a history record with an invalid index."""
        # Try to delete from an empty DataFrame
        with self.assertRaises(IndexError):
            self.command_handler.delete_calculation_by_index(5)

    def test_load_plugin(self):
        """Test loading a valid plugin."""
        with patch('importlib.import_module') as mock_import_module:
            mock_module = MagicMock()
            mock_import_module.return_value = mock_module

            result = self.command_handler.load_plugin('TestPlugin')

            # Ensure the plugin was loaded
            mock_import_module.assert_called_with('app.plugins.TestPlugin')
            self.assertEqual(result, mock_module.register())

    def test_load_plugin_invalid(self):
        """Test loading an invalid plugin."""
        with patch('importlib.import_module', side_effect=ImportError):
            result = self.command_handler.load_plugin('InvalidPlugin')

            # Ensure that an ImportError is handled
            self.assertIsNone(result)

    def test_load_plugin_register(self):
        """Test loading a plugin and creating an instance via register."""
        with patch('importlib.import_module') as mock_import_module:
            mock_module = MagicMock()
            mock_import_module.return_value = mock_module
            mock_module.register.return_value = MagicMock()

            result = self.command_handler.load_plugin_register('TestPlugin', 5, 10)

            # Ensure the plugin was loaded and an instance was created
            mock_import_module.assert_called_with('app.plugins.TestPlugin')
            mock_module.register.assert_called_with(self.command_handler)
            self.assertIsNotNone(result)

    @patch.dict(os.environ, {}, clear=True)
    def test_export_to_csv(self):
        """Test exporting history to CSV."""
        # Add a history record
        self.command_handler.add_history('Add', 5, 10, 15)

        # Export history to CSV
        result = self.command_handler.export_to_csv('Test-History.csv')

        # Verify that the file was created and data was exported
        self.assertTrue(os.path.exists('Test-History.csv'))
        self.assertEqual(result, 'History exported to Test-History.csv')

    @patch.dict(os.environ, {}, clear=True)
    def test_import_from_csv(self):
        """Test importing history from CSV."""
        # Simulate a CSV file with history data
        # Simulate a CSV file with history data
        csv_data = 'Operation,Value1,Value2,Result\nAdd,5,10,15\nSubtract,20,5,15\n'
        with open('Test-History.csv', 'w', encoding='utf-8') as file:  # Specify the encoding explicitly
            file.write(csv_data)

        # Import history from the CSV file
        result = self.command_handler.import_from_csv('Test-History.csv')

        # Verify that the data was imported into the DataFrame
        self.assertEqual(len(self.command_handler.history_df), 2)
        self.assertEqual(result.iloc[0]['Operation'], 'Add')
        self.assertEqual(result.iloc[1]['Operation'], 'Subtract')

if __name__ == "__main__":
    unittest.main()
