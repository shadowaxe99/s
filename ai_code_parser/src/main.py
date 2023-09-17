
import sys
from gpt3_interface import GPT3Interface
from code_parser import CodeParser

def main():
    # Get the user's context
    context = input("Please provide context on what you want functionally: ")

    # Initialize the GPT3 interface
    gpt3 = GPT3Interface()

    # Initialize the code parser
    parser = CodeParser()

    # Parse the code from the repos
    code_snippets = parser.parse_repos()

    # Get instructions from GPT3
    instructions = gpt3.get_instructions(code_snippets, context)

    # Print the instructions
    print(instructions)

if __name__ == "__main__":
    main()
