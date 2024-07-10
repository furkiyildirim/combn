# Combination Generator

This project is a Python application that generates all possible combinations of a certain length using a specific character set. The combinations are saved to a file and the program can resume from where it left off when reopened.

## Requirements

- Python 3.x
- `itertools` module (standard library in Python)

## Installation

To run this project, you don't need to install any additional dependencies. Just make sure that Python 3.x is installed.

## Usage

1. Download or clone the project files.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the `main.py` file:


## Structure

- `main.py`: The main program that generates and saves combinations to a file. It can resume from where it left off.
- `combinations.json`: The file where combinations are saved.
- `progress.json`: The file that keeps track of the program's progress.

## Warning

This program may require a lot of RAM to generate a large number of combinations. Make sure you have enough RAM on your system. Otherwise, the program may slow down or crash. The RAM usage will increase as the combination length increases. Therefore, be careful when running long combinations and limit the n value if necessary.

### Example:

1. For a combination of a certain length, there are 72 combinations (26 lowercase letters + 26 uppercase letters + 10 digits + 10 symbols).
2. For a combination of a certain length, there are 5184 combinations (26 lowercase letters + 26 uppercase letters + 10 digits + 10 symbols)^2.
3. For a combination of a certain length, there are 373248 combinations (26 lowercase letters + 26 uppercase letters + 10 digits + 10 symbols)^3.

The RAM usage will increase as the combination length increases. Therefore, be careful when running long combinations and limit the n value if necessary.
