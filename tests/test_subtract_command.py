"""
Unit tests for SubtractCommand functionality.
"""

import unittest
import logging
import pandas as pd
from app.commands import CommandHandler
from app.plugins.Subtract import register  # Removed unused imports

# Disable logging for tests
logging.disable(logging.CRITICAL)

class TestSubtractCommand(unittest.TestCase):
    """Unit tests for SubtractCommand to test subtraction functionality."""

    def setUp(self):
        """Set up a CommandHandler instance and register the SubtractCommand."""
        self.command_handler = CommandHandler()  # Create a CommandHandler instance
        self.subtract_command_creator = register(self.command_handler)  # Register the SubtractCommand

    def test_subtract_normal(self):
        """Test subtracting two positive numbers."""
        subtract_command = self.subtract_command_creator(10, 5)  # Subtract 10 - 5

        # Execute the command and check the result
        result = subtract_command.execute()
        self.assertEqual(result, 5, "10 - 5 should result in 5.")

        # Verify the result is added to the history
        expected_history = pd.DataFrame({
            'Operation': ['Subtract'],
            'Value1': [10.0],
            'Value2': [5.0],
            'Result': [5.0]
        })
        pd.testing.assert_frame_equal(self.command_handler.history_df, expected_history, check_dtype=False)

    def tearDown(self):
        """Clean up after each test."""
        self.command_handler.clear_history()
    def test_subtract_zero(self):
        """Test subtracting zero from a number."""
        subtract_command = self.subtract_command_creator(10, 0)  # Subtract 10 - 0

        # Execute the command and check the result
        result = subtract_command.execute()
        self.assertEqual(result, 10, "10 - 0 should result in 10.")

        # Verify the result is added to the history
        expected_history = pd.DataFrame({
            'Operation': ['Subtract'],
            'Value1': [10.0],
            'Value2': [0.0],
            'Result': [10.0]
        })
        pd.testing.assert_frame_equal(self.command_handler.history_df, expected_history, check_dtype=False)

    def test_subtract_negative(self):
        """Test subtracting a negative number from another number."""
        subtract_command = self.subtract_command_creator(10, -5)  # Subtract 10 - (-5)

        # Execute the command and check the result
        result = subtract_command.execute()
        self.assertEqual(result, 15, "10 - (-5) should result in 15.")

        # Verify the result is added to the history
        expected_history = pd.DataFrame({
            'Operation': ['Subtract'],
            'Value1': [10.0],
            'Value2': [-5.0],
            'Result': [15.0]
        })
        pd.testing.assert_frame_equal(self.command_handler.history_df, expected_history, check_dtype=False)

    def test_subtract_large_numbers(self):
        """Test subtracting two large numbers."""
        subtract_command = self.subtract_command_creator(1e10, 5e9)  # Subtract 1e10 - 5e9

        # Execute the command and check the result
        result = subtract_command.execute()
        self.assertEqual(result, 5e9, "1e10 - 5e9 should result in 5e9.")

        # Verify the result is added to the history
        expected_history = pd.DataFrame({
            'Operation': ['Subtract'],
            'Value1': [1e10],
            'Value2': [5e9],
            'Result': [5e9]
        })
        pd.testing.assert_frame_equal(self.command_handler.history_df, expected_history, check_dtype=False)
if __name__ == "__main__":
    unittest.main()
