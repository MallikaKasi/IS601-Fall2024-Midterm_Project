## Welcome to Command-Plugin based Interactive Calculator Application With Environment Variables Loading, Logging and Continuous Integration Concepts 

This is the interactive Calculator that performs the functions.

Addition

Subtraction

Multiplication

Division

### This Calculator can run in 2 modes

1) Interactive Mode which is implemented using plugins

2) Implementation of command pattern and REPL

Added a main.py file to serve as an entry point to this program and provided command line utilities.

Covers REPL and command patterns with four basic commands add, subtract, multiply and divide.

Implements a menu command to list available command and usage example.

Implemented Greet and Exit Commands

Uses Plugin architecture to dynamically load new plugins.

Uses .env file to set environment variables

Logging using Logger library.These logging statements will help us to trace the flow of the program and identify any issues.

Continuous Integration using GitHub Actions workflow to run tests on GitHub automatically.

### Testing Commands:

pytest 

pytest --pylint

pytest --pylint --cov

pytest tests/test_main.py.


### Run the Applications:
To run the Interactive Calculator: python main.py I

To perform the calculation directly from Command Line:  python main.py 2 3 add

## Environmental Variables
Environmental Variables are loaded in the main.py. Environmental variables are loaded from the .env file. Environmental variables are also used in the configure logging method. logging_conf_path is an environmental variable and is used to determine the path to the logging config file.

![image](https://github.com/user-attachments/assets/dca9f425-ccbd-4034-a74e-e6b0df8b9432)
![image](https://github.com/user-attachments/assets/6be590a2-7f6e-412c-a9a2-2e261b2a7036)
![image](https://github.com/user-attachments/assets/e2372103-615f-41c4-9bc8-0472a1c01e89)

## Logging
Logging is used print INFO, WARNING and Error messages. Info letting them know how the interactive calculator works and how to execute the list of commands in the menu options. Logging is also used as a warning and sends them an error message if they input an invalid command. Examples are shown below.
![image](https://github.com/user-attachments/assets/9621dba2-8c70-4074-aa03-4f7854c20787)

![image](https://github.com/user-attachments/assets/70acd646-0cdf-41e5-a7ec-5e1250ed4ac2)

### Test Results:

![image](https://github.com/user-attachments/assets/1dc929b9-acb1-4eb2-af0d-e08c35ef9678)
![image](https://github.com/user-attachments/assets/6d483887-aff6-4e55-a44f-ccd181d81bf5)
![image](https://github.com/user-attachments/assets/cc98b3c3-321b-4110-877d-8d445faaa142)


### Output Log File
![image](https://github.com/user-attachments/assets/e2d23f6a-2859-47c4-b89c-f851406bb6d4)
![image](https://github.com/user-attachments/assets/8b60a342-467b-4497-966b-5894d9616ce2)






