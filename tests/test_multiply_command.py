"""
Unit tests for MultiplyCommand functionality.
"""

import unittest
import logging
import pandas as pd
from app.commands import CommandHandler
from app.plugins.Multiply import register  # Removed unused imports

# Disable logging for tests
logging.disable(logging.CRITICAL)

class TestMultiplyCommand(unittest.TestCase):
    """Unit tests for MultiplyCommand to test multiplication functionality."""

    def setUp(self):
        """Set up a CommandHandler instance and register the MultiplyCommand."""
        self.command_handler = CommandHandler()  # Create a CommandHandler instance
        self.multiply_command_creator = register(self.command_handler)  # Register the MultiplyCommand

    def test_multiply_normal(self):
        """Test multiplying two positive numbers."""
        multiply_command = self.multiply_command_creator(10, 5)  # Multiply 10 * 5

        # Execute the command and check the result
        result = multiply_command.execute()
        self.assertEqual(result, 50, "10 * 5 should result in 50.")

        # Verify the result is added to the history
        expected_history = pd.DataFrame({
            'Operation': ['Multiply'],
            'Value1': [10.0],
            'Value2': [5.0],
            'Result': [50.0]
        })
        pd.testing.assert_frame_equal(self.command_handler.history_df, expected_history, check_dtype=False)

    def tearDown(self):
        """Clean up after each test."""
        self.command_handler.clear_history()

if __name__ == "__main__":
    unittest.main()
