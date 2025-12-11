from sunlang import *

def main():
    source = "IF+-123 foo*THEN/"
    sun = Sunlang(source)

    token = sun.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = sun.getToken()

main()