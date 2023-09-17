
import os
import ast

class CodeParser:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.parsed_code = []

    def parse_directory(self, path):
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.py'):
                    self.parse_file(os.path.join(root, file))

    def parse_file(self, file_path):
        with open(file_path, 'r') as file:
            file_content = file.read()
            self.parsed_code.append(ast.parse(file_content))

    def get_parsed_code(self):
        return self.parsed_code

    def run(self):
        self.parse_directory(self.repo_path)

