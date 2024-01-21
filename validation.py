from operations.operationsFactory import OperationsFactory
from stringManipulation import splitMathExpression, replaceUnaryMinusesWithUnderscore, signCorrection


def findWrongSymbol(expression: str):
    wrong_symbols = []
    factory_instance = OperationsFactory()
    for i in expression:
        if not i.isnumeric() and not factory_instance.isExists(i) and i != '.':
            wrong_symbols.append(i)

    return wrong_symbols


def findWrongUnaryRightPlaceSymbol(expression: str):
    wrong_symbols = []
    legit_right_symbols = ['#', '!']
    binary_symbols = ['+', '-', '*', '/', '^', '%', '@', '$', '&']
    for i in range(len(expression) - 1):
        if i != 0:

            if (expression[i] in legit_right_symbols
                    and (not expression[i - 1].isnumeric() and not expression[i + 1] in legit_right_symbols and
                         expression[i - 1] != ')')):
                wrong_symbols.append(expression[i])

            elif (expression[i] in legit_right_symbols
                  and (not expression[i + 1] in binary_symbols and not expression[i + 1] in legit_right_symbols and
                       expression[i + 1] != '(')):
                wrong_symbols.append(expression[i])
    return wrong_symbols


def findWrongUnaryLeftPlaceSymbol(expression: str):
    wrong_symbols = []
    exp = signCorrection(expression)
    exp = replaceUnaryMinusesWithUnderscore(exp)
    legit_left_symbols = ['_', '~']
    binary_symbols = ['+', '-', '*', '/', '^', '%', '@', '$', '&']
    for i in range(len(exp) - 1):
        if i != 0:
            if (exp[i] == '~'
                    and exp[i + 1] == '_' and not exp[i - 1].isnumeric()):
                i += 1
            if (exp[i] == '_'
                    and exp[i - 1] == '~' and exp[i + 1].isnumeric()):
                i += 1

            elif (exp[i] in legit_left_symbols
                  and not exp[i - 1] in binary_symbols and exp[i - 1] != '('):
                wrong_symbols.append(expression[i])
            elif (exp[i] == '-'
                  and exp[i + 1] == '~'):
                wrong_symbols.append(expression[i])

            elif (exp[i] in legit_left_symbols
                  and (not exp[i + 1].isnumeric() and exp[i + 1] != '(')):
                wrong_symbols.append(expression[i])

    return wrong_symbols


def countParenthesis(expression: str):
    counter = 0
    for i in expression:
        if i == '(':
            counter += 1
        elif i == ')':
            counter -= 1
            if counter < 0:
                return False

    return counter == 0


def nearParenthesis(expression: str):
    for i in range(len(expression) - 1):
        if i != 0:
            if expression[i] == '(' and (expression[i - 1].isnumeric() or expression[i - 1] == ")"):
                return False
            elif expression[i] == ')' and (expression[i + 1].isnumeric() or expression[i + 1] == '('):
                return False
    return True


def emptyParenthesis(expression: str):
    for i in range(len(expression)):

        if expression[i] == '(' and expression[i + 1] == ')':
            return False
    return True


def canNotBeInEdges(expression: str):
    wrong_symbols = []
    legit_right_edge = ['-', '~', '(']
    legit_left_edge = [')', '!', '#']
    if expression[0] not in legit_right_edge and not expression[0].isnumeric():
        wrong_symbols.append(expression[0])
    elif expression[- 1] not in legit_left_edge and not expression[- 1].isnumeric():
        wrong_symbols.append(expression[- 1])

    return wrong_symbols


def validate_exp(exp: str):
    if len(exp) == 0:
        raise ValueError(f'exp is empty ')

    invalid_chars = findWrongSymbol(exp)
    if len(invalid_chars) != 0:
        raise ValueError(f'{invalid_chars}  Unacceptable Symbol ')

    invalid_chars = findWrongUnaryRightPlaceSymbol(exp)
    if len(invalid_chars) != 0:
        raise SyntaxError(f'{invalid_chars}  Wrong Unary Right Place ')
    invalid_chars = findWrongUnaryLeftPlaceSymbol(exp)
    if len(invalid_chars) != 0:
        raise SyntaxError(f'{invalid_chars}  Wrong Unary Left Place ')

    if not countParenthesis(exp):
        raise SyntaxError('parenthesis are not balanced ')

    if not nearParenthesis(exp):
        raise SyntaxError('parenthesis are not in place ')

    if not emptyParenthesis(exp):
        raise SyntaxError('empty parenthesis ')

    invalid_chars = canNotBeInEdges(exp)
    if len(invalid_chars) != 0:
        raise SyntaxError(f'{invalid_chars}  can not be in edge')
