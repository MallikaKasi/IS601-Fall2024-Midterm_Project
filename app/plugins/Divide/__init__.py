import logging
from app.commands import Command
from icecream import ic
from app.commands import CommandHandler

class DivideCommand(Command):
    def __init__(self, a, b, command_handler: CommandHandler):
        """Initialize the DivideCommand with two numbers."""
        self.a = a
        self.b = b
        self.command_handler = command_handler  # Store the command handler instance

    def execute(self):
        """Perform division and handle division by zero."""
        try:
            if self.b == 0:
                raise ValueError("Unable to divide by 0")
            
            result = self.a / self.b
            print(f"    The result of Dividing {self.a} / {self.b} = {result}")
            # Use the CommandHandler instance to store the result in history
            self.command_handler.add_history('Divide', self.a, self.b, result)

            # Log the result
            logging.info(f"Invoked Divide Operation")
            logging.info(f"The result of dividing {self.a} / {self.b} = {result}")
            logging.info(f"Division Reslult is : {ic(self.a / self.b)}")

            return result  # Return the result of the division
        except ValueError as e:
            # Log the error and raise it again to notify the caller
            logging.error(f" {e}")
            raise

def register(command_handler: CommandHandler):
    """Return a function that creates AddCommand instances with the command handler."""
    return lambda a, b: DivideCommand(a, b, command_handler)
