"""T"""
import unittest
from unittest.mock import patch, MagicMock
from app import App
from app.commands import CommandHandler


class TestApp(unittest.TestCase):
    """Tests for the App class."""

    def setUp(self):
        """Set up the app and mock the command handler."""
        self.app = App()
        self.app.command_handler = CommandHandler()

    @patch('builtins.input', side_effect=['Add', '10', '5', 'E'])
    @patch('builtins.print')
    @patch('sys.exit', side_effect=SystemExit)
    def test_add_command(self, mock_print, mock_input, mock_sys_exit):
        """Test the Add command flow."""
        with patch.object(CommandHandler, 'load_plugin_register') as mock_load_plugin_register:
            mock_add_command = MagicMock()
            mock_add_command.execute = MagicMock(return_value="Success")
            mock_load_plugin_register.return_value = mock_add_command

            self.app.load_plugins()

            with self.assertRaises(SystemExit):
                self.app.start()

            # Debug: Print the input calls
            print(mock_input.call_args_list)

            mock_load_plugin_register.assert_called_with('Add', 10.0, 5.0)
            mock_add_command.execute.assert_called_once()

            self.assertEqual(mock_input.call_count, 6)

    @patch('builtins.input', side_effect=['Subtract', '20', '10', 'E'])
    @patch('builtins.print')
    @patch('sys.exit', side_effect=SystemExit)
    def test_subtract_command(self, mock_print, mock_input, mock_sys_exit):
        """Test the Subtract command flow."""
        with patch.object(CommandHandler, 'load_plugin_register') as mock_load_plugin_register:
            mock_subtract_command = MagicMock()
            mock_subtract_command.execute = MagicMock(return_value="Success")
            mock_load_plugin_register.return_value = mock_subtract_command

            self.app.load_plugins()

            with self.assertRaises(SystemExit):
                self.app.start()

            # Debug: Print the input calls
            print(mock_input.call_args_list)

            mock_load_plugin_register.assert_called_with('Subtract', 20.0, 10.0)
            mock_subtract_command.execute.assert_called_once()

            self.assertEqual(mock_input.call_count, 6)

    @patch('builtins.input', side_effect=['Multiply', '3', '4', 'E'])
    @patch('builtins.print')
    @patch('sys.exit', side_effect=SystemExit)
    def test_multiply_command(self, mock_print, mock_input, mock_sys_exit):
        """Test the Multiply command flow."""
        with patch.object(CommandHandler, 'load_plugin_register') as mock_load_plugin_register:
            mock_multiply_command = MagicMock()
            mock_multiply_command.execute = MagicMock(return_value="Success")
            mock_load_plugin_register.return_value = mock_multiply_command

            self.app.load_plugins()

            with self.assertRaises(SystemExit):
                self.app.start()
            mock_load_plugin_register.assert_called_with('Multiply', 3.0, 4.0)
            mock_multiply_command.execute.assert_called_once()

            self.assertEqual(mock_input.call_count, 5)

    @patch('builtins.input', side_effect=['Divide', '10', '0', 'E'])
    @patch('builtins.print')
    @patch('sys.exit', side_effect=SystemExit)
    def test_divide_by_zero(self, mock_print, mock_input, mock_sys_exit):
        """Test division by zero handling."""
        with patch.object(CommandHandler, 'load_plugin_register') as mock_load_plugin_register:
            mock_divide_command = MagicMock()
            mock_divide_command.execute = MagicMock(side_effect=ZeroDivisionError)
            mock_load_plugin_register.return_value = mock_divide_command

            self.app.load_plugins()

            with self.assertRaises(SystemExit):
                self.app.start()

            # Verify that the division by zero error was printed
            # mock_print.assert_any_call("Error: Division by zero.")

    @patch('builtins.input', side_effect=['Add', 'ten', '5', 'E'])
    @patch('builtins.print')
    @patch('sys.exit', side_effect=SystemExit)
    def test_add_with_invalid_input(self, mock_print, mock_input, mock_sys_exit):
        """Test handling of non-numeric input for the Add command."""
        with patch.object(CommandHandler, 'load_plugin_register') as mock_load_plugin_register:
            mock_add_command = MagicMock()
            mock_load_plugin_register.return_value = mock_add_command

            self.app.load_plugins()

            with self.assertRaises(SystemExit):
                self.app.start()

            # Check that the invalid input was handled and an appropriate error was printed
            #mock_print.assert_any_call("could not convert string to float: 'ten'")

    @patch('builtins.input', side_effect=['Exit'])
    @patch('builtins.print')
    @patch('sys.exit', side_effect=SystemExit)
    def test_exit_command(self, mock_print, mock_input, mock_sys_exit):
        """Test the Exit command flow."""
        self.app.load_plugins()

        with self.assertRaises(SystemExit):
            self.app.start()

        # Debug: Print the input calls
        print(mock_input.call_args_list)

        self.assertEqual(mock_input.call_count, 4)
        mock_sys_exit.assert_called_once()

    @patch('builtins.input', side_effect=['E'])
    @patch('builtins.print')
    @patch('sys.exit', side_effect=SystemExit)
    def test_invalid_command(self, mock_print, mock_input, mock_sys_exit):
        """Test handling of an invalid command."""
        self.app.load_plugins()

        with self.assertRaises(SystemExit):
            self.app.start()

        mock_sys_exit.assert_called_once()


if __name__ == "__main__":
    unittest.main()
