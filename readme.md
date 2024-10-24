## Welcome to Interactive Calculator Application 

This is the interactive Calculator that performs various functions.The calculator is a fully functional calculator that can perform basic arithmetic operations, stores history, gets history, deletes history, imports history from a csv file, and exports history from a csv file. The calculator also displays a user friendly menu options.

	Greet : To Perform Greet Operation

	Menu : To List the Menu options

	Add : To Perform Addition

	Multiply : To Perform Multiplication

	Subtract : To Perform Subtraction

	Divide : To Perform Division

	History : To load the saved History Data

	ClearHistory : Clear the History details

	DeleteFromHistory : Delete History from the Dataframe / CSV file

	Exit : To Perform Exit Operation


### This Calculator runs in 2 modes

i) Interactive Mode which is implemented using plugins

ii) Implementation of command pattern and REPL to perform Add, Subtract, Multiply and Division.

## Main Features of this Project:

1. REPL Command-Line Interface (CLI)
   
	The Read-Eval-Print Loop (REPL) provides an intuitive command-line interface that allows users to perform arithmetic operations like addition, subtraction, multiplication, and division.
	Access builtin commands like viewing the history, importing/exporting history, and clearing or deleting it.
	Added a main.py file to serve as an entry point to this program and provided command line utilities.
	Covers REPL and command patterns with four basic commands add, subtract, multiply and divide.
	
2. Plugin and Builtin Module System
   
   	 Uses Plugin architecture to dynamically load new plugins and allow seamless integration of new commands or features.
   	 Has a Menu command to list available command and usage examples.
   	Implemented Greet and Exit Commands

3. Design Patterns & Best Practices
 
   	Facade Pattern: Simplifies interactions between the application and the pandas data manipulation logic, allowing for a cleaner, more manageable interface.
	DRY Principle: The code follows the "Don't Repeat Yourself" principle to ensure reusability and maintainability.
	Look Before You Leap (LBYL) & Easier to Ask for Forgiveness than Permission (EAFP): These techniques are used to handle potential errors efficiently by checking for conditions before performing 		operations and catching exceptions where appropriate.

4. Environment Variables Loading and Logging/ Error Handling
   
	Uses .env file to set environment variables
	Logging using Logger library.These logging statements will help us to trace the flow of the program and identify any issues.

5. Continuous Integration
   
   	Using GitHub Actions workflow to run tests on GitHub automatically.

6. Calculation History Management
   	Using Pandas library for Dataframe loading , CSV file export and import functions for History Management . Functions To Load, save, clear, and delete history records through the REPL interface.

7. Version Control
	Git Best Practices: This project is maintained using Git version control. Best practices such as branching for feature development and using logical, meaningful commit messages were followed throughout 	the project lifecycle.
8. Testing
	Test Coverage: The application is thoroughly tested using the pytest framework. All modules, functions, and features have been tested with a coverage rate of 92%.
	Code Quality: The codebase adheres to PEP 8 standards, ensuring readability and maintainability. Testing also includes running pylint to maintain code quality.

## To Run the Applications:

	To run the Interactive Calculator: python main.py I

	To perform the calculation directly from Command Line:  python main.py 2 3 add

## Command-Line Interface (REPL) :

	Implemented a Read-Eval-Print Loop (REPL) to facilitate direct interaction with the calculator to

	To Perform arithmetic operations (Add, Subtract, Multiply, and Divide)

	Management of calculation history.

## Design Patterns

### Command Design Pattern

This project utilizes the Command design pattern in many places. All the operation functions utilize the command class. Example below is from the Add Command Code.

![image](https://github.com/user-attachments/assets/b1df4678-897d-4b6c-9655-86b784f0e3d6)

### Factory Design Pattern

Loading of plugins from plugin directories and creates instances of their classes without specifying their concrete class. Example is shown below.

![image](https://github.com/user-attachments/assets/0bcde930-6867-4523-b855-3b3899cb5886)

### Facade Design Pattern

Facade design pattern been used for the complicated operations such as writing the history data to the specified csv file or importing data from a CSV file and interacting with Pandas DataFrames. Below is the code snippet.

![image](https://github.com/user-attachments/assets/382c56bc-5110-416d-b345-331231e523ec)

## DRY, LBYL, EAFP

There are many cases where DRY,LBYL and EAFP design principles are used in this project. Examples are mentioned below for reference.

**DRY (Don't Repeat Yourself)** : principle is followed in the entire project. Below is the code snippet where plugin loading function is written as common code and has been called in mulplitple times.

![image](https://github.com/user-attachments/assets/5ab5ba7a-583d-4358-8191-710a7ce22398)
![image](https://github.com/user-attachments/assets/837fa53a-9410-4da3-9238-6c3c860f9b54)


**EAFP (Easier to Ask for Forgiveness than Permission)** : Try and except blocks.Try executes the command without checking for errors and if an error occurs, an exception is raised as shown in except block. The code will execute the command, however, If a user does not type in a valid command, an exception is raised and an error message is printed out.

![image](https://github.com/user-attachments/assets/8e35792c-b792-4e70-b519-e77d9205b788)
![image](https://github.com/user-attachments/assets/27801fa0-806b-4a5c-aa17-2327a0a92419)


**LBYL (Look Before You Leap)** : This first checks to see if the logging configuration file present before it attempts to load it. If the config file exists, then loads the logging configuration otherwise default to a basic logging configuration.

![image](https://github.com/user-attachments/assets/28b4654e-c5eb-4ea5-9014-95fc497a3252)


## Environmental Variables

Environmental Variables are loaded in the main.py. Environmental variables are loaded from the .env file. Environmental variables are also used in the configure logging method. logging_conf_path is an environmental variable and is used to determine the path to the logging config file.

![image](https://github.com/user-attachments/assets/dca9f425-ccbd-4034-a74e-e6b0df8b9432)
![image](https://github.com/user-attachments/assets/6be590a2-7f6e-412c-a9a2-2e261b2a7036)
![image](https://github.com/user-attachments/assets/e2372103-615f-41c4-9bc8-0472a1c01e89)

## Logging
Logging is used print INFO, WARNING and Error messages. Info letting them know how the interactive calculator works and how to execute the list of commands in the menu options. Logging is also used as a warning and sends them an error message if they input an invalid command. Examples are shown below.

![image](https://github.com/user-attachments/assets/9621dba2-8c70-4074-aa03-4f7854c20787)

![image](https://github.com/user-attachments/assets/70acd646-0cdf-41e5-a7ec-5e1250ed4ac2)

### Testing Commands:

pytest 

pytest --pylint

pytest --pylint --cov

pytest tests/test_main.py.

### Test Results:

![image](https://github.com/user-attachments/assets/1dc929b9-acb1-4eb2-af0d-e08c35ef9678)
![image](https://github.com/user-attachments/assets/6d483887-aff6-4e55-a44f-ccd181d81bf5)
![image](https://github.com/user-attachments/assets/cc98b3c3-321b-4110-877d-8d445faaa142)


### Sample Log File output

![image](https://github.com/user-attachments/assets/e2d23f6a-2859-47c4-b89c-f851406bb6d4)
![image](https://github.com/user-attachments/assets/8b60a342-467b-4497-966b-5894d9616ce2)


### My Calculator App Video Demonstration
[TBA]




