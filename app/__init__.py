import pkgutil
import importlib
from app.commands import CommandHandler, Command
import logging
import multiprocessing
import os

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.plugins = []  # List to store the names of loaded plugins
   
    def load_plugins(self):
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                logging.info(f"Loading plugin: {plugin_name}")  # Add logging to see the loading process
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if plugin_name == "Menu":
                            self.command_handler.register_command(plugin_name, item(self.command_handler))
                        else:
                            self.command_handler.register_command(plugin_name, item())
                        self.plugins.append(plugin_name)  # Add loaded plugin to the list
                    except (TypeError, AttributeError):
                        continue

    def execute_command(self, command_name, *args):
        try:
            command = self.command_handler.create_command(command_name, *args)
            return self.command_handler.execute_command(command_name)
        except ZeroDivisionError:
            logging.error("Error: Division by zero.")
            print("Error: Division by zero.")
        except ValueError as e:
            print(e)
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            print(f"An error occurred: {e}")

    def start(self):
        self.load_plugins()
        self.command_handler.execute_command("Menu")

        while True:  # REPL Read, Evaluate, Print, Loop
            choice = input("Choose an option: ")
            if choice == 'C':
                continue
            elif choice == 'E' or choice == 'Exit':
                self.execute_command('Exit')
                break
            elif choice in ['Add', 'Subtract', 'Multiply', 'Divide', 'Greet', 'Menu']:
                if choice in ['Add', 'Subtract', 'Multiply', 'Divide']:
                    a = float(input("   Enter the first number: "))
                    b = float(input("   Enter the second number: "))
                    self.execute_command(choice, a, b)
                else:
                    self.execute_command(choice)
            else:
                # Invalid command, should NOT call execute_command
                logging.warning("Invalid choice. Please select a valid option.")
                print("Invalid choice. Please select a valid option.")
                continue  # Make sure to loop without calling execute_command


def start_app():
    app = App()
    app.start()

if __name__ == "__main__":  # For running in a separate process
    multiprocessing.Process(target=start_app).start()
