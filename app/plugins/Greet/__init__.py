import logging
from app.commands import Command

class GreetCommand(Command):
    def execute(self):
        greeting_message = "     Hello! Welcome To Interactive Calculator"
        
        # Log the operation
        logging.info("Invoked Greet Operation")
        logging.info(greeting_message)
        
        # Print the greeting to the console
        print(greeting_message)
        
        # Return the greeting message
        return greeting_message

def register():
    return GreetCommand