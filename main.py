from filesystem import InMemoryFileSystem

def main():
    file_system = InMemoryFileSystem()
    print("Welcome to the In-Memory File System!")

    while True:
        command = input("Enter command (type 'exit' to quit): ")
        
        if command.lower() == "exit":
            print("Exiting...")
            break

        try:
            if command.startswith("mkdir"):
               _, directory_name = command.split(" ", 1)
               file_system.mkdir(directory_name)

            elif command.startswith("cd"):
                _, path = command.split(" ", 1)
                file_system.cd(path)

            elif command.startswith("ls"):
                path = command.split(" ", 1)[1] if len(command.split(" ")) > 1 else "."
                contents = file_system.ls(path)
                print("Contents:", contents)

            elif command.startswith("grep"):
                _, pattern, file_path = command.split(" ", 2)
                result = file_system.grep(pattern, file_path)
                print("Pattern found:", result)

            elif command.startswith("cat"):
                 _, file_path = command.split(" ", 1)
                 content = file_system.cat(file_path)
                 print("File content:", content)

            elif command.startswith("touch"):
                 _, file_path = command.split(" ", 1)
                 file_system.touch(file_path)

            elif command.startswith("echo"):
                 _, text, file_path = command.split(" ", 2)
                 file_system.echo(text, file_path)

            elif command.startswith("mv"):
                 _, source_path, destination_path = command.split(" ", 2)
                 file_system.mv(source_path, destination_path)

            elif command.startswith("cp"):
                 _, source_path, destination_path = command.split(" ", 2)
                 file_system.cp(source_path, destination_path)
            
            elif command.startswith("rm"):
                 _, path = command.split(" ", 1)
                 file_system.rm(path)

            else:
                print("Invalid command. Please try again.")

            pass

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

