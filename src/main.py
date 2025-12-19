from lexer import *
from emit import *
from parser import *
import sys

def main():
    print("Sunlang Compiler!")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument!")
    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()

    lexer = Lexer(source)
    emiter = Emitter("out.c")
    parser = Parser(lexer, emiter)

    parser.program()
    emiter.writeFile()
    print("Parsing Completed")

main()