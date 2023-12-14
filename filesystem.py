import os
import re


class File:
    def __init__(self, name, content=""):
        self.name = name
        self.content = content


class Directory:
    def __init__(self, name):
        self.name = name
        self.children = {}  # Dictionary to store child files and directories


class InMemoryFileSystem:
    def __init__(self):
        self.root = Directory("/")
        self.current_directory = self.root

    def mkdir(self, directory_name):
        new_directory = Directory(directory_name)
        self.current_directory.children[directory_name] = new_directory

    def cd(self, path):
        if path == "..":
            self.current_directory = self._get_parent_directory(self.current_directory)
        elif path == "/":
            self.current_directory = self.root
        else:
            target_directory = self._get_absolute_path_from_root(path)
            if target_directory:
                self.current_directory = target_directory

    def ls(self, path="."):
        target_directory = self._get_absolute_path(path)
        contents = [item.name for item in target_directory.children.values()]
        return contents

    def grep(self, pattern, file_path):
        target_file = self._get_absolute_path(file_path)
        if isinstance(target_file, File):
            return re.search(pattern, target_file.content)

    def cat(self, file_path):
        target_file = self._get_absolute_path(file_path)
        if isinstance(target_file, File):
            return target_file.content

    def touch(self, file_path):
        new_file_name = os.path.basename(file_path)
        new_file = File(new_file_name)
        self.current_directory.children[new_file_name] = new_file

    def echo(self, text, file_path):
        target_file = self._get_absolute_path(file_path)
        if isinstance(target_file, File):
            target_file.content = text

    def mv(self, source_path, destination_path):
        source = self._get_absolute_path(source_path)
        destination_directory = self._get_absolute_path(destination_path)

        if isinstance(source, (File, Directory)):
            destination_directory.children[source.name] = source
            del self._get_parent_directory(self._get_absolute_path(source_path)).children[source.name]

    def cp(self, source_path, destination_path):
        source = self._get_absolute_path(source_path)
        destination_directory = self._get_absolute_path(destination_path)

        if isinstance(source, (File, Directory)):
            destination_directory.children[source.name] = source

    def rm(self, path):
        target = self._get_absolute_path(path)
        if isinstance(target, (File, Directory)):
            del self._get_parent_directory(target).children[target.name]

    def _get_absolute_path(self, path):
        if path.startswith("/"):
            return self._get_absolute_path_from_root(path)
        else:
            return self._get_absolute_path_from_current(path)

    def _get_absolute_path_from_root(self, path):
        current_directory = self.root
        components = path.strip("/").split("/")
        for component in components:
            if component == "..":
                current_directory = self._get_parent_directory(current_directory)
            else:
                current_directory = current_directory.children.get(component, None)
                if current_directory is None:
                    return None
        return current_directory

    def _get_absolute_path_from_root(self, path):
        components = path.strip("/").split("/")
        current_directory = self.root

        for component in components:
            if component == "..":
                current_directory = self._get_parent_directory(current_directory)
            else:
                current_directory = current_directory.children.get(component, None)
                if current_directory is None:
                    return None  # Directory not found

        return current_directory

    def _get_parent_directory(self, node):
        if node == self.root:
            return self.root

        for directory in self.root.children.values():
            if node in directory.children.values():
                return directory




