import importlib
from abc import ABC, abstractmethod
import logging
import pandas

# Command interface definition
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# CommandHandler class
class CommandHandler:
    def __init__(self):
        self.commands = {}  # Dictionary to store command instances
        self.dtypes = {
            'Operation': 'str',
            'Value1': 'float',
            'Value2': 'float',
            'Result': 'float'
        }
        self.history_df = pandas.DataFrame(columns=['Operation', 'Value1', 'Value2', 'Result']).astype(self.dtypes)

    def register_command(self, command_name: str, command_instance: Command):
        self.commands[command_name] = command_instance  # Store command instance by name

    def execute_command(self, command_name: str):
        if command_name in self.commands:
            self.commands[command_name].execute()  # Execute the command instance
        else:
            logging.info(f"No such command: {command_name}")
            print(f"No such command: {command_name}")
            return

    def load_plugin(self, plugin_name):
        # Dynamically load plugin from the plugins folder
        try:
            plugin_module = importlib.import_module(f"app.plugins.{plugin_name}")
            command_class = plugin_module.register()  # Ensure register() returns a Command class
            return command_class  # Return the class, not an instance
        except ImportError as e:
            print(f"Failed to load plugin {plugin_name}: {e}")
        except AttributeError:
            print(f"Plugin {plugin_name} is missing the 'register()' function.")
            raise
    
    def load_plugin_register(self, plugin_name, a, b):
        # Dynamically load plugin from the plugins folder
        try:
            plugin_module = importlib.import_module(f"app.plugins.{plugin_name}")
            command_class = plugin_module.register(self)  # Ensure register() returns a Command class
            if command_class:
                command_instance = command_class(a,b)  # Instantiate the command class
                return command_instance
            else:
                raise ValueError(f"Failed to create command: {plugin_name}")
            return command_class  # Return the class, not an instance
        except ImportError as e:
            print(f"Failed to load plugin {plugin_name}: {e}")
        except AttributeError:
            print(f"Plugin {plugin_name} is missing the 'register()' function.")
            raise

    def create_command(self, plugin_name, *args):
        command_class = self.load_plugin(plugin_name)  # Load the plugin's command class
        if command_class:
            command_instance = command_class(*args)  # Instantiate the command class
            self.register_command(plugin_name, command_instance)  # Register the instance
            return command_instance
        else:
            raise ValueError(f"Failed to create command: {plugin_name}")

    def list_commands(self):
        """Logs and prints all available commands."""
        all_commands = "\nAvailable Calculator Commands:\n"  # Initialize the string for commands
        all_commands += '\n'.join([f"    Type {key} : To Perform {key} Operation" for key in self.commands]) + '\n'
        
        # Log and print the available commands
        logging.info(all_commands)
        print(all_commands)

    def add_history(self, operation, a, b, result):
        """Add a command result to the history DataFrame, avoiding duplicates."""
        # Checks to see if the record already exists in the DataFrame to avoid duplicates
        if not ((self.history_df['Operation'] == operation) & 
                (self.history_df['Value1'] == a) & 
                (self.history_df['Value2'] == b) & 
                (self.history_df['Result'] == result)).any():
            # If not a duplicate, creates a new record
            new_record = pandas.DataFrame({
                'Operation': [operation],
                'Value1': [a],
                'Value2': [b],
                'Result': [result]
            }, columns=['Operation', 'Value1', 'Value2', 'Result'])
            
            self.history_df = pandas.concat([self.history_df, new_record], ignore_index=True)

    def get_history(self):
        """Return the history of operations as a formatted string."""
        if self.history_df.empty:
            print(f"No calculations are available. Please enter a command")
            return "No calculations are available. Please enter a command."
        else:
            self.export_to_csv("History.csv")
            #return self.history_df.to_string(index=True)
            return self.import_from_csv("History.csv")

    def clear_history(self):
        """Clear the calculation history."""
        self.history_df = self.history_df.iloc[0:0]  # Clear the DataFrame
        logging.info("Cleared history.")
    
    def delete_from_history(self):
            if self.history_df.empty:
                    print("No history available to delete.")
                    return            
            print(self.history_df)  # Show all calculations with indexes for user reference
            
            try:
                index_to_delete = int(input("Enter the index of the calculation to delete: "))
                self.delete_calculation_by_index(index_to_delete - 1)
                print(f"Calculation at index {index_to_delete} has been deleted.")
            except ValueError:
                print("Invalid index. Enter a valid index or 'exit' to return to history menu.")
            except IndexError:
                print("No calculation found at the given index.")    


    def display_all_calculations(self):
            all_calculations = self.get_history()
            if all_calculations:
                print("\nAll Calculations:")
                for idx, calculation in enumerate(all_calculations, start=1):
                    try:
                        result = calculation.compute()
                        print(f"{idx}. {calculation} results in {result}")  # Format this based on how your calculations are stored/represented
                    except ZeroDivisionError:
                        print(f"{idx}. {calculation} is undefined")
            else:
                print("No calculations in history.")
    
    def delete_calculation_by_index(self, index: int):
        """Delete a calculation from the history by its index.

        Args:
            index (int): The index of the calculation to delete.
        """
        if 0 <= index < len(self.history_df):
            # Delete the row at the given index and reset the index
            self.history_df.drop(index , inplace=True)
            self.history_df.reset_index(drop=True, inplace=True)  # Reset the index
            print("Updated History:")
            print(self.history_df)
        else:
            raise IndexError("Calculation index out of range.")

    def export_to_csv(self, filepath):
        try:
            self.history_df.to_csv(filepath, index=False)
            return f"History exported to {filepath}"
        except Exception as e:
            return f"Failed to export history to CSV: {str(e)}"
    
    def import_from_csv(self, filepath):
        try:
            # Load new history
            new_history = pandas.read_csv(filepath)

            # Check columns
            if set(new_history.columns) == {'Operation', 'Value1', 'Value2', 'Result'}:
                # Standardize and clean data
                new_history = new_history.astype(self.dtypes)
                new_history['Operation'] = new_history['Operation'].str.strip()

                #print("New history before merging:")
                #print(new_history)

                # Check for pre-existing duplication
                if not new_history.duplicated(subset=['Operation', 'Value1', 'Value2', 'Result']).any():
                    print("No duplicates in the new history.")
                else:
                    print("Duplicates detected in the new history.")

                # Combine with existing history and remove duplicates
                combined_history = pandas.concat([self.history_df, new_history], ignore_index=True)
                combined_history = combined_history.drop_duplicates(subset=['Operation', 'Value1', 'Value2', 'Result'])

                # Assign the combined history
                self.history_df = combined_history

                #print("History after merging:")
                #print(self.history_df)
                print(f"History successfully imported from {filepath}")
                return self.history_df
            else:
                return "Invalid CSV format. Ensure the columns are 'Operation', 'Value1', 'Value2', and 'Result'."
        except Exception as e:
            return f"Failed to import history from CSV: {str(e)}"
