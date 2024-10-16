import logging
from app.commands import Command

class DivideCommand(Command):
    def __init__(self, a, b):
        """Initialize the DivideCommand with two numbers."""
        self.a = a
        self.b = b

    def execute(self):
        """Perform division and handle division by zero."""
        try:
            if self.b == 0:
                raise ValueError("Unable to divide by 0")
            
            result = self.a / self.b
            print(f"    The result of Dividing {self.a} / {self.b} = {result}")
            
            # Log the result
            logging.info(f"Invoked Divide Operation")
            logging.info(f"The result of dividing {self.a} / {self.b} = {result}")

        except ValueError as e:
            # Log the error and raise it again to notify the caller
            logging.error(f" {e}")
            raise

def register():
    """Register the DivideCommand."""
    return DivideCommand
