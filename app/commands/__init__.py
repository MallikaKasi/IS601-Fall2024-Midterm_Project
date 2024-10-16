import importlib
from abc import ABC, abstractmethod
import logging

# Command interface definition
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# CommandHandler class
class CommandHandler:
    def __init__(self):
        self.commands = {}  # Dictionary to store command instances
    
    def register_command(self, command_name: str, command_instance: Command):
        if not isinstance(command_instance, Command):
            raise TypeError(f"Invalid command instance: {command_instance}")
        self.commands[command_name] = command_instance

    def execute_command(self, command_name: str):
        if command_name in self.commands:
            return self.commands[command_name].execute()  # Execute the command instance
        else:
            print(f"No such command: {command_name}")

    def load_plugin(self, plugin_name):
        """Dynamically load a single plugin."""
        try:
            plugin_module = importlib.import_module(f"app.plugins.{plugin_name}")
            command_class = plugin_module.register()  # Ensure register() returns a Command class
            return command_class  # Return the class, not an instance
        except ImportError as e:
            logging.error(f"Failed to load plugin {plugin_name}: {e}")
            return None
        except AttributeError as e:
            logging.error(f"Plugin {plugin_name} is missing the 'register()' function: {e}")
            return None


    def create_command(self, plugin_name, *args):
        command_class = self.load_plugin(plugin_name)  # Load the plugin's command class
        if command_class:
            command_instance = command_class(*args)  # Instantiate the command class
            self.register_command(plugin_name, command_instance)  # Register the instance
            return command_instance
        else:
            raise ValueError(f"Failed to create command: {plugin_name}")
        
    def list_commands(self):
        #print("              ")
        #print("Available Calculator Commands:")
        #print(" ")
        #logging.info(f"Available Menu Options in Interactive Calculator:")

        for key in self.commands:
            all_commands = '\n\n' + '\n'.join([f"    Type {key} : To Perform {key} Operation" for key in self.commands]) + '\n'
        logging.info(all_commands)


    # Creating a dictionary
    my_Menu_dict = {
        'Greet' : '1',
        'Menu' : '2',
        'Add' : '3',
        'Subtract' : '4',
        'Multiply' : '5',
        'Divide' : '6',
        'Exit' :  '7'
    }
    