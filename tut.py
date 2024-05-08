#!/usr/local/bin/python3
# ! ^^ Above is the shebang line, it tells the terminal how to interpret the script
# ! It is not normaly needed because the extension of the file tells the terminal how to interpret it
# ! But when a file does not have an extension, like this one, it is needed to tell the terminal where to find the interpreter

import os, sys, subprocess

# ? OS: for working with the operating system / terminal
# ? SYS: for working with system specific parameters and functions
# ? SUBPROCESS: for running other programs from python, like bash commands

# * GOAL
# * - Create a script that when run will create a directory with an inputed name
# * - Inside this directory will be a file called "main.py"
# * - This file will contain the following code:
# * - print("Hello World")
# * - exit(0) # exit with 0, meaning no error occured

print(sys.argv[0]) # prints script path
args = sys.argv[1:] # [1:] removes own script path from list

if len(args) == 0: # //! if no arguments are given
    print("No arguments given")
    exit(1) # exit with error code 1, meaning an error occured

if len(args) > 1: # //! if more than one argument is given
    print("Too many arguments given")
    exit(1) # exit with error code 1, meaning an error occured

if len(args) == 1:
    directory_name = args[0] # get the first argument
    
    os.mkdir(directory_name) # create the directory with the given name
    
    os.chdir(directory_name) # change the working directory to the new directory
    
    with open("main.py", "w") as python_file: # //* create a new file called "main.py" and open it for writing, if it does not exist it will be created
        python_file.write("print('Hello World')\nexit(0)")
    
    subprocess.run(["python3", "main.py"]) # ? run the file with python3, this is the same as pressing play in an IDE

    exit(0) # exit with 0, meaning no error occured