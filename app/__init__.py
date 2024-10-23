import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command
import logging
#from app.plugins.Add import register

#from app.plugins.menu import MenuCommand
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
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        #if issubclass(item, (Command)) and item is not Command:  # Added extra condition as it was registering the command twice
                            if (plugin_name == "Menu" or plugin_name == "History" or plugin_name == "ClearHistory" or plugin_name == "DeleteFromHistory" ):
                                self.command_handler.register_command(plugin_name, item(self.command_handler))
                            else:
                                self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore
            
    
    
    def start(self):
        self.load_plugins()
        self.command_handler.execute_command("Menu")
        
        choice = input("Choose an option : ")
        while True:   #REPL Read, Evaluate, Print, Loop
            try:
                if choice == 'C':
                    choice = input("Choose an option : ")
                    continue
                elif choice == 'Add':
                    a = float(input("   Enter the first number: "))
                    b = float(input("   Enter the second number: "))
                    Add_Command = self.command_handler.load_plugin_register('Add', a, b)
                    Add_Command.execute()
                elif choice == 'Subtract':
                    a = float(input("   Enter the first number: "))
                    b = float(input("   Enter the second number: "))
                    Subtract_Command = self.command_handler.load_plugin_register('Subtract', a, b)
                    Subtract_Command.execute()
                elif choice == 'Multiply':
                    a = float(input("   Enter the first number: "))
                    b = float(input("   Enter the second number: "))
                    Multiply_Command = self.command_handler.load_plugin_register('Multiply', a, b)
                    Multiply_Command.execute()
                elif choice == 'Divide':
                    a = float(input("   Enter the first number: "))
                    b = float(input("   Enter the second number: "))
                    Divide_Command = self.command_handler.load_plugin_register('Divide', a, b)
                    Divide_Command.execute()
                elif choice == 'Exit' or choice == 'E':
                    exit_command = self.command_handler.create_command('Exit')
                    result = self.command_handler.execute_command('Exit')
                elif choice == 'Greet':
                    Greet_command = self.command_handler.create_command('Greet')
                    result = self.command_handler.execute_command('Greet')
                elif choice == 'Menu':
                    result = self.command_handler.execute_command('Menu')
                elif choice == 'History':
                    result = self.command_handler.execute_command('History')
                elif choice == 'ClearHistory':
                    result = self.command_handler.execute_command('ClearHistory')
                elif choice == 'DeleteFromHistory':
                    result = self.command_handler.execute_command('DeleteFromHistory')
                else:
                    logging.warning("Invalid choice. Please select a valid option.")
            except ZeroDivisionError:
                    logging.error("Error: Division by zero.")
                    print("Error: Division by zero.")
            except ValueError as e:
                print(e)
            except Exception as e:
                print(f"An error occurred: {e}")
            print(" ")
            print("Type C : to Continue , Type E : to Exit  ")

            choice = input("")


def start_app():
    app = App()
    app.start()

if __name__ == "__main__":
    multiprocessing.Process(target=start_app).start()