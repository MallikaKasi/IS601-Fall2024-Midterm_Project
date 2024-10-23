import logging
from app.commands import Command
from app.commands import CommandHandler

class SubtractCommand(Command):
    def __init__(self, a, b, command_handler: CommandHandler):
        """Initialize the SubtractCommand with two numbers."""
        self.a = a
        self.b = b
        self.command_handler = command_handler  # Store the command handler instance

    def execute(self):
        """Perform subtraction and log the result."""
        result = self.a - self.b
        print(f"    The result of Subtracting {self.a} - {self.b} = {result}")
        # Use the CommandHandler instance to store the result in history
        self.command_handler.add_history('Subtract', self.a, self.b, result)
        
        # Log the subtraction result
        logging.info(f"Invoked Subtract Operation")
        logging.info(f"    The result of subtracting {self.a} - {self.b} is {result}")
        return result
def register(command_handler: CommandHandler):
    """Return a function that creates AddCommand instances with the command handler."""
    return lambda a, b: SubtractCommand(a, b, command_handler)

