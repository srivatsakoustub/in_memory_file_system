                                                    Implementation Overview of In-Memory File System
                                    
Design Philosophy
The primary goal was to create a lightweight, easy-to-use, in-memory file system in Python, emphasizing simplicity, clarity, and standard file system functionalities.


Data Structures and Classes :-
File Class: Represents a file with two attributes: name (string) and content (string).

Directory Class: Represents a directory. It has name (string) and children (dictionary), where keys are names of files/directories, and values are File or Directory instances.

InMemoryFileSystem Class: The core class, handling all file system operations


Functionalities
Mkdir: Creates a new directory in the current directory.
Cd: Changes the current working directory.
Ls: Lists contents of a directory.
Grep: Searches for text within a file (bonus).
Cat: Displays the content of a file.
Touch: Creates a new file.
Echo: Writes text to a file.
Mv: Moves files or directories.
Cp: Copies files or directories.
Rm: Removes files or directories


Improvements to the Design
Error Handling: Enhanced to handle various edge cases like invalid paths, nonexistent files, and permission issues.
Efficiency: Optimized navigation methods for quicker access to directories and files.
Scalability: Designed to easily accommodate additional features or commands in the future.
User Experience: Improved command-line interface for clearer interaction.


To run and test the program I’ve written in Visual Studio Code, follow these steps:
Create a Python File: If you haven’t already, create a new Python file (`.py`) in VS Code. You can do this by clicking on the “New File” icon and selecting Python as the file type.

Code references a class called `InMemoryFileSystem`. This class needs to be implemented for your code to work. Make sure you have this class defined in your project, either in the same file or in a separate Python file that you import.

Run the Program: You can run the program in VS Code by right-clicking on the Python file and selecting “Run Python File in Terminal” or by pressing `F5` to run in debug mode.

Interact with the Program: Once the program is running, it will wait for your commands in the terminal. You can test the different functionalities like `mkdir`, `cd`, `ls`.as defined in your code.


Debugging: If you encounter errors, use the debugging tools in VS Code to step through your code and understand where the issues are.

Exit the Program: Type `exit` in the command prompt of your program to terminate the execution.

for the program to work correctly, all functions called (like `mkdir`, `cd`, ) must be properly implemented in the `InMemoryFileSystem` class.

Created a Dockerfile for a memory file system, build an image from it using VS Code, and pushed it to a repository
https://hub.docker.com/repository/docker/srivatsakoustub/in_file_memory_system_1/general

