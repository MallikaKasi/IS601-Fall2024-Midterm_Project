# app/plugins/ClearHistory.py
import logging

from app.commands import Command
from app.commands import CommandHandler

class ClearHistoryCommand(Command):
    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler

    def execute(self):
        logging.info(f"Invoked Clear History Operation")
        self.command_handler.clear_history()


def register(command_handler: CommandHandler):
    return ClearHistoryCommand(command_handler)  # Return the class, not an instance
