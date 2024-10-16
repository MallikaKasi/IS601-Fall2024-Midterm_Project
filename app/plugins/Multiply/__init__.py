import logging
from app.commands import Command

class MultiplyCommand(Command):
    def __init__(self, a, b):
        """Initialize the MultiplyCommand with two numbers."""
        self.a = a
        self.b = b

    def execute(self):
        """Perform multiplication and log the result."""
        result = self.a * self.b
        print(f"    The result of Multiplying {self.a} * {self.b} = {result}")
        
        # Log the multiplication result
        logging.info(f"Invoked Multiply Operation")
        logging.info(f"    The result of multiplying {self.a} * {self.b} is {result}")
        return result 

def register():
    """Register the MultiplyCommand."""
    return MultiplyCommand
