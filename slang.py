from utils import arguments
from core.lexer import SLexer
from core.parser import SParser
from core.eval import SEval

arg = arguments.args(
    "file_name",
    "Give the name of the file that you want to run.")

# arg.file_nam => gives the arg
def main():
    filename = arg.file_name
    file     = open(filename, 'r')

    lexer = SLexer(file)
    parser = SParser(lexer.token)

    lexer.tokenizer()
    print("Tokens: ")
    print(f"{lexer.token} \n")

    parser.build_AST()
    print(f"AST: {parser.AST}")

    evaluator = SEval(parser.AST)
if __name__ == "__main__":
    main()