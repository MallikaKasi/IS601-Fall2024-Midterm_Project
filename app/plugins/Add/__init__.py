import logging
from app.commands import Command
from app.commands import CommandHandler

class AddCommand(Command):
    def __init__(self, a, b, command_handler: CommandHandler):
        """Initialize the AddCommand with two numbers and a CommandHandler instance."""
        self.a = a
        self.b = b
        self.command_handler = command_handler  # Store the command handler instance

    def execute(self):
        """Perform the addition and log the result."""
        result = self.a + self.b
        print(f"    The result of adding {self.a} + {self.b} = {result}")
        
        # Log the addition operation
        logging.info(f"Invoked Add Operation")
        logging.info(f"The result of adding {self.a} + {self.b} = {result}")
        # Use the CommandHandler instance to store the result in history
        self.command_handler.add_history('Add', self.a, self.b, result)

def register(command_handler: CommandHandler):
    """Return a function that creates AddCommand instances with the command handler."""
    return lambda a, b: AddCommand(a, b, command_handler)
