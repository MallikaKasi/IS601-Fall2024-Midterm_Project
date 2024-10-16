"""
Unit tests for the GreetCommand in the Greet plugin.
"""

import pytest
from app.commands import CommandHandler

@pytest.fixture
def command_handler():
    """Fixture to create and return a CommandHandler instance."""
    handler = CommandHandler()
    handler.load_plugin('Greet')  # Load the 'Greet' plugin
    return handler

def test_greet_command(command_handler, capsys):
    """Test the GreetCommand to ensure greeting works."""
    command_handler.create_command('Greet')
    result = command_handler.execute_command('Greet')

    # Assert the return value of the command is the expected greeting
    assert result == "     Hello! Welcome To Interactive Calculator"

    # Capture and assert the print output
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello! Welcome To Interactive Calculator"
