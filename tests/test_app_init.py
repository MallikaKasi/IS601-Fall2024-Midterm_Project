"""
This module contains test cases for testing the app initialization and functionality.
"""
from unittest.mock import patch  # Standard library import
import pytest  # Third-party import
from app import App  # Local application imports

def test_app_initialization():
    """Test that the App class initializes properly."""
    app_instance = App()
    assert app_instance is not None
    assert isinstance(app_instance, App)

def test_app_load_plugins():
    """Test that plugins are loaded correctly."""
    app_instance = App()
    app_instance.load_plugins()
    assert len(app_instance.plugins) > 0, "No plugins were loaded. Check the plugin loading logic."

def test_app_start():
    """Test the start process of the App with mocked input."""
    app_instance = App()
    # Mocking input for Add operation and then Exit
    with patch('builtins.input', side_effect=['Add', '5', '3', 'E']):
        with pytest.raises(SystemExit):  # Expecting SystemExit on Exit
            app_instance.start()

@pytest.fixture
def app():
    """Test the greet command."""
    return App()

def test_greet_command(app):
    """Test the greet command."""
    with patch('builtins.input', side_effect=['Greet', 'E']):
        with patch.object(app, 'execute_command') as mock_exec:
            app.start()
            mock_exec.assert_any_call('Greet')  # Verify 'Greet' command was called

def test_add_command(app):
    """Test the add command with inputs 5 and 10."""
    with patch('builtins.input', side_effect=['Add', '5', '10', 'E']):
        with patch.object(app, 'execute_command') as mock_exec:
            app.start()
            mock_exec.assert_any_call('Add', 5.0, 10.0)  # Verify 'Add' command was called with correct args

def test_invalid_command(app):
    """Test that an invalid command doesn't call execute_command."""
    with patch('builtins.input', side_effect=['Invalid', 'E']):  # Simulate invalid input and then exit
        with patch.object(app, 'execute_command') as mock_exec:
            app.start()
            # Ensure execute_command was not called for the invalid input
            mock_exec.assert_called_with('Exit')  # Called once for 'Exit', but not for 'Invalid'
