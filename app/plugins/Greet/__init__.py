""" Greet """
import logging
from app.commands import Command

class GreetCommand(Command):
    """Command to print and log a greeting message."""
    
    def execute(self):
        """Print and return a greeting message."""
        greeting_message = "Hello! Welcome to the Interactive Calculator."
        
        # Log the operation
        logging.info("Invoked Greet Operation")
        logging.info(greeting_message)
        
        # Print the greeting to the console
        print(greeting_message)
        
        # Return the greeting message for testing purposes
        return greeting_message

def register():
    """Register the GreetCommand."""
    return GreetCommand()
