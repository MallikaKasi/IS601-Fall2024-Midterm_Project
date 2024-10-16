# app/plugins/menu.py
import logging

from app.commands import Command
from app.commands import CommandHandler

class MenuCommand(Command):
    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler

    def execute(self):
        logging.info(f"Invoked Menu Operation")
        logging.info(f"Listing Below the Available Menu Commands in Calculator Application")
        self.command_handler.list_commands()


def register():
    return MenuCommand  # Return the class, not an instance
