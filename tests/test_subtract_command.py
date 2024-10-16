"""Test the SubtractCommand with positive and negative values."""
#from unittest.mock import patch
#import pytest
from app.plugins.Subtract import SubtractCommand

def test_subtract_command(capsys):
    """Test the SubtractCommand with positive and negative values."""
    subtract_command = SubtractCommand(10, 5)
    subtract_command.execute()

    captured = capsys.readouterr()
    assert captured.out.strip() == "The result of Subtracting 10 - 5 = 5"

    subtract_command_neg = SubtractCommand(-5, -10)
    subtract_command_neg.execute()

    captured = capsys.readouterr()
    assert captured.out.strip() == "The result of Subtracting -5 - -10 = 5"
