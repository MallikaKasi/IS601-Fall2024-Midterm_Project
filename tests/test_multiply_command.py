"""
Unit tests for the MultiplyCommand in the Multiply plugin.
"""

import pytest  # Third-party imports
from app.commands import CommandHandler  # Local imports

@pytest.fixture
def command_handler():
    """Fixture to create and return a CommandHandler instance."""
    handler = CommandHandler()
    handler.load_plugin('Multiply')  # Load the 'Multiply' plugin
    return handler

def test_multiply_by_zero(command_handler):
    """Test multiplying by zero."""
    a, b = 10, 0
    command_handler.create_command('Multiply', a, b)
    result = command_handler.execute_command('Multiply')
    assert result == 0

def test_multiply_negative(command_handler):
    """Test multiplying by a negative number."""
    a, b = -5, 3
    command_handler.create_command('Multiply', a, b)
    result = command_handler.execute_command('Multiply')
    assert result == -15
