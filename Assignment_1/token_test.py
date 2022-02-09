def readFileCreateTokens(filename):
    
    keywords = ['and', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
                ' exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
                'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']

    operators = ['+', '-', '*', '/', '%', '**', '//', '<<', '>>', '&', 
                '|', '^', '~', '<', '<=', '>', '>=', '<>', '!=', '==']
    
    delimiters = ['(', ')', '[', ']', '{', '}', ',', ':', '.', '`', '=', ';', '+=', 
                '-=', '*=', '/=', '//=', '%=', '&=', '|=', '^=', '>>=', '<<=', '**=']

    separators = [' ', '    ', '\n']

    identifiers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    tokens = []
    lines = []

    with open(filename) as f:
        for line in f:
            lines.extend(line.split())


    #print(lines)

    for row, line in enumerate(lines):
        for col, element in enumerate(line):
            if element in separators:
                continue
            elif element in keywords:
                type = 'keyword'
            elif element in operators:
                type = 'operator'
            elif element in delimiters:
                type = 'delimiter'
            elif element in identifiers:
                type = 'identifier'
                tokens.append([type, line, row, col])
                break

            tokens.append([type, element, row, col])
    
    return tokens

print(readFileCreateTokens('seaCondition.txt'))