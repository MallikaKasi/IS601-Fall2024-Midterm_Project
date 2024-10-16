"""
Unit tests for the DivideCommand in the Divide plugin.
"""

import logging  # Standard library import
import pytest  # Third-party import
from app.plugins.Divide import DivideCommand  # Local import

def test_divide_success(caplog):
    """Test successful division of two numbers."""
    a, b = 10, 2
    divide_command = DivideCommand(a, b)

    # Execute the command and capture logs
    with caplog.at_level(logging.INFO):
        divide_command.execute()

    assert "The result of dividing 10 / 2 = 5.0" in caplog.text  # Check logs
    assert caplog.records[0].levelname == "INFO"  # Ensure the log level is INFO

def test_divide_by_zero():
    """Test division by zero, should raise a ValueError."""
    a, b = 10, 0
    divide_command = DivideCommand(a, b)

    # Test that dividing by zero raises a ValueError
    with pytest.raises(ValueError, match="Unable to divide by 0"):
        divide_command.execute()

def test_logging_divide_by_zero(caplog):
    """Test that division by zero is properly logged."""
    a, b = 10, 0
    divide_command = DivideCommand(a, b)

    # Execute the command and capture logs
    with caplog.at_level(logging.ERROR):
        with pytest.raises(ValueError):
            divide_command.execute()

    assert "Unable to divide by 0" in caplog.text  # Check if error is logged
    assert caplog.records[0].levelname == "ERROR"  # Ensure the log level is ERROR
