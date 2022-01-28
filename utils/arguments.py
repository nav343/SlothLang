'''
Importing the ArgParse module to get arguments while running the program.
'''
from argparse import ArgumentParser

# Defining parser variable.....
parser = ArgumentParser(
    description="SlLang, a general purpose programming language.")

def args(arg1: str, help_text: str = "A help command"):
    parser.add_argument(
        arg1, 
        help=help_text)

    args = parser.parse_args()
    return args
