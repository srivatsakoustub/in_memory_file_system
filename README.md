Design Philosophy
The primary goal was to create a lightweight, easy-to-use, in-memory file system in Python, emphasizing simplicity, clarity, and standard file system functionalities.

The code defines a simple command-line interface for an in-memory file system using the InMemoryFileSystem class.

The program runs in a loop, continuously taking user input for commands until the user types 'exit' to quit.

Supported commands include creating directories (mkdir), changing the current directory (cd), listing contents (ls), searching for patterns in files (grep), displaying file content (cat), creating files (touch), appending text to files (echo), moving/renaming files or directories (mv), copying files or directories (cp), and removing files or directories (rm).

The code catches exceptions and prints error messages if the entered command is invalid or if an error occurs during command execution.

The program provides a basic file system interaction experience, allowing users to perform various file and directory operations in-memory through the command-line interface.

