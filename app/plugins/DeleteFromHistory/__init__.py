# app/plugins/menu.py
import logging

from app.commands import Command
from app.commands import CommandHandler

class DeleteFromHistoryCommand(Command):
    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler

    def execute(self):
        logging.info(f"Invoked Delete from History Operation")
        self.command_handler.delete_from_history()


def register(command_handler: CommandHandler):
    return DeleteFromHistoryCommand(command_handler)  # Return the class, not an instance
