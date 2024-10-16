import os
import socket
import sys
import logging
import logging.config
from decimal import Decimal, InvalidOperation
from dotenv import load_dotenv
from app.calculator import Calculator
from app import App

class OperationCommand:
    def __init__(self, calculator=None, operation_name=None, a=None, b=None):
        self.calculator = calculator
        self.operation_name = operation_name
        self.a = a
        self.b = b

        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.set_hostname_in_env()

    def get_computer_name(self):
        """Get the computer's hostname."""
        return socket.gethostname()

    def set_hostname_in_env(self):
        """Set the computer name as the hostname in environment variables."""
        computer_name = self.get_computer_name()
        os.environ['HOSTNAME'] = computer_name
        logging.info(f"Hostname set to: {computer_name}")

    def load_environment_variables(self):
        """Load environment variables into a dictionary."""
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded")
        return settings

    def get_environment_variable(self):
        """Get the ENVIRONMENT variable."""
        return self.settings.get('ENVIRONMENT', 'Not set')

    def get_hostname_variable(self):
        """Get the HOSTNAME variable."""
        return self.settings.get('HOSTNAME', 'Not set')

    def print_env_variables(self):
        """Print the environment variables."""
        print(f"ENVIRONMENT: {self.get_environment_variable()}")
        print(f"HOSTNAME: {self.get_hostname_variable()}")

    def configure_logging(self):
        """Configure logging for the application."""
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, 
                                format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Application started")
        logging.info("Logging configured")

    def execute(self):
        """Execute the operation using the calculator."""
        operation_method = getattr(self.calculator, self.operation_name, None)
        if operation_method:
            return operation_method(self.a, self.b)
        else:
            logging.error(f"Unknown operation: {self.operation_name}")
            raise ValueError(f"Unknown operation: {self.operation_name}")

def calculate_and_print(a, b, operation_name):
    """Perform a calculation and print the result."""
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        command = OperationCommand(Calculator, operation_name, a_decimal, b_decimal)
        logging.info(f"Performing  {operation_name} Operation")
        result = command.execute()
        print(f"The result of {a} {operation_name} {b} is equal to {result}")
        logging.info(f"The result of {a} {operation_name} {b} is equal to {result}")

    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
        logging.error("Invalid number input: {a} or {b} is not a valid number.")
       
    except ZeroDivisionError:
        print("Error: Division by zero.")
        logging.error("Error: Division by zero.")

    except ValueError as e:
        print(e)
    except Exception as e:
        #print(f"An error occurred: {e}")
        logging.error(f"An error occurred: {e}")

def main():
    """Main function to run the application."""

    if len(sys.argv) == 2:
        command = OperationCommand()
        logging.info("Welcome to Interactive Calculator Application:")
        app_instance = App()
        app_instance.start()
    elif len(sys.argv) == 4:
        _, a, b, operation_name = sys.argv
        calculate_and_print(a, b, operation_name)
    else:
            command = OperationCommand()
            logging.info("Welcome to Interactive Calculator Application:")
            print(f"Incorrect Number of arguments , So Exiting the Application")

            logging.error(""" Incorrect Number of arguments , So Exiting the Application
                    
                    Correct Usage of this Calculator Application:
                     
                    To start the Interactive Calculator: python main.py I
                    To perform the Operation Using Direct Command Line :
                                
                        python main.py <number1> <number2> add
                        python main.py <number1> <number2> subtract
                        python main.py <number1> <number2> multiply
                        python main.py <number1> <number2> divide
                """)

            sys.exit(1)

if __name__ == '__main__':
    main()
