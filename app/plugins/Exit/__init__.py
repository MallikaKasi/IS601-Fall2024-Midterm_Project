import logging
import sys
from app.commands import Command


class ExitCommand(Command):
    def execute(self):
        logging.info(f"Exiting the Application...Goodbye!!!!!")

        sys.exit("Exiting the Application...Goodbye!!!!!")

def register():
    return ExitCommand
