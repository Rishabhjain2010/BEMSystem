import os

def clear_terminal():
    # Clear the terminal screen based on the operating system
    if os.name == 'posix':  # For UNIX/Linux/Mac
        os.system('clear')
    elif os.name == 'nt':  # For Windows
        os.system('cls')
