import re

#Task 7
def readFileCreateTokens(filename):

    keywords = ['and', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
                'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
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
    rows = []
    cols = []

    with open(filename) as f:
        for line in f:
            lines.extend([line.split()])
    
    print(lines)

    row = 1
    for line in lines:
        #print('line: ', line)
        col = 1
        for word in line:
            print("Word: ", word)
            for element in word:

                if element in separators:
                    continue
                elif element in keywords:
                    type = 'keyword'
                elif element in operators:
                    type = 'operator'
                elif element in delimiters:
                    type = 'delimiter'
                elif element in identifiers:
                
                #[['lol', 'pikk'], ['lol', 'pikk'], ['lol', 'pikk']]

                    type = 'identifier'
                    if word[-1] in delimiters:
                        tokens.append([type, word[:-1], row, col])
                        type = 'delimiter'
                        tokens.append([type, word[-1], row, col])
                        col += len(word)

                        break
                    tokens.append([type, word, row, col])
                    col += len(word)
                    break

                tokens.append([type, word, row, col])
                col += len(word)
        row += 1
    return tokens


#print(readFileCreateTokens('seaCondition.txt'))
numbers = re.findall('[0-1]+', )
print(numbers)