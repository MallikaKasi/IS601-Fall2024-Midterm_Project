import logging
from app.commands import Command

class SubtractCommand(Command):
    def __init__(self, a, b):
        """Initialize the SubtractCommand with two numbers."""
        self.a = a
        self.b = b

    def execute(self):
        """Perform subtraction and log the result."""
        result = self.a - self.b
        print(f"    The result of Subtracting {self.a} - {self.b} = {result}")
        
        # Log the subtraction result
        logging.info(f"Invoked Subtract Operation")
        logging.info(f"    The result of subtracting {self.a} - {self.b} is {result}")

def register():
    """Register the SubtractCommand."""
    return SubtractCommand
