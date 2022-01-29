from utils import arguments
from core.lexer import SLexer
from core.parser import SParser
from core.eval import SEval
from colorama import Fore, Style

arg = arguments.args(
    "file_name",
    "Give the name of the file that you want to run.")

try:
# arg.file_nam => gives the arg
    def main():
        filename = arg.file_name
        file     = open(filename, 'r')

        lexer = SLexer(file)
        parser = SParser(lexer.token)

        lexer.tokenizer()

        parser.build_AST()

        evaluator = SEval(parser.AST)
        evaluator.run(parser.AST)


    if __name__ == "__main__":
        main()

except Exception:
    print(Fore.RED + "An Error occurred.")
    print(Fore.RED + "File Executed with code 1")
    print(Style.RESET_ALL)