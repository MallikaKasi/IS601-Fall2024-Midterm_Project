import logging
from app.commands import Command

class AddCommand(Command):
    def __init__(self, a, b):
        """Initialize the AddCommand with two numbers."""
        self.a = a
        self.b = b

    def execute(self):
        """Perform the addition and log the result."""
        result = self.a + self.b
        print(f"    The result of adding {self.a} + {self.b} = {result}")
        
        # Proper f-string usage for logging
        logging.info(f"Invoked Add Operation")

        logging.info(f"The result of adding {self.a} + {self.b} = {result}")

def register():
    """Register the AddCommand."""
    return AddCommand
