import logging
from app.commands import Command
from app.commands import CommandHandler

class MultiplyCommand(Command):
    def __init__(self, a, b, command_handler: CommandHandler):
        """Initialize the MultiplyCommand with two numbers."""
        self.a = a
        self.b = b
        self.command_handler = command_handler  # Store the command handler instance

    def execute(self):
        """Perform multiplication and log the result."""
        result = self.a * self.b
        print(f"    The result of Multiplying {self.a} * {self.b} = {result}")
        # Use the CommandHandler instance to store the result in history
        self.command_handler.add_history('Multiply', self.a, self.b, result)
        
        # Log the multiplication result
        logging.info(f"Invoked Multiply Operation")
        logging.info(f"    The result of multiplying {self.a} * {self.b} is {result}")
        return result 

def register(command_handler: CommandHandler):
    """Return a function that creates AddCommand instances with the command handler."""
    return lambda a, b: MultiplyCommand(a, b, command_handler)
