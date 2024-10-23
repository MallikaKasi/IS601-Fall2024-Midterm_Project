"""
Unit tests for DivideCommand functionality.
Tests include normal division, division by zero, and negative number division.
"""

import unittest
import logging
import pandas as pd
from app.commands import CommandHandler
from app.plugins.Divide import register  # Removed DivideCommand, if not directly used

# Disable logging for tests
logging.disable(logging.CRITICAL)

class TestDivideCommand(unittest.TestCase):
    """Unit tests for DivideCommand to test different division scenarios."""

    def setUp(self):
        """Set up a CommandHandler instance and register the DivideCommand."""
        self.command_handler = CommandHandler()  # Create a CommandHandler instance
        self.divide_command_creator = register(self.command_handler)  # Register the DivideCommand

    def test_divide_normal(self):
        """Test dividing two positive numbers."""
        divide_command = self.divide_command_creator(10, 2)  # Divide 10 / 2

        # Execute the command and check the result
        result = divide_command.execute()
        self.assertEqual(result, 5, "10 / 2 should result in 5.")

        # Verify the result is added to the history
        expected_history = pd.DataFrame({
            'Operation': ['Divide'],
            'Value1': [10.0],
            'Value2': [2.0],
            'Result': [5.0]
        })
        pd.testing.assert_frame_equal(self.command_handler.history_df, expected_history, check_dtype=False)

    def test_divide_by_zero(self):
        """Test dividing by zero which should raise a ValueError."""
        divide_command = self.divide_command_creator(10, 0)  # Divide 10 / 0

        # Expect a ValueError due to division by zero
        with self.assertRaises(ValueError) as context:
            divide_command.execute()

        # Check if the exception message is correct
        self.assertEqual(str(context.exception), "Unable to divide by 0")

        # Verify that no operation was added to the history after division by zero
        self.assertTrue(self.command_handler.history_df.empty, "No entry should be added to the history when dividing by zero.")

    def test_divide_negative_numbers(self):
        """Test dividing negative and positive numbers."""
        divide_command = self.divide_command_creator(-10, 2)  # Divide -10 / 2

        # Execute the command and check the result
        result = divide_command.execute()
        self.assertEqual(result, -5, "-10 / 2 should result in -5.")

        # Verify the result is added to the history
        expected_history = pd.DataFrame({
            'Operation': ['Divide'],
            'Value1': [-10.0],
            'Value2': [2.0],
            'Result': [-5.0]
        })
        pd.testing.assert_frame_equal(self.command_handler.history_df, expected_history, check_dtype=False)

    def tearDown(self):
        """Clean up after each test."""
        self.command_handler.clear_history()

if __name__ == "__main__":
    unittest.main()
