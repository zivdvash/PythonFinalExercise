"""
Validation module for mathematical expressions.

Includes functions to find and validate various aspects of mathematical expressions,
such as wrong symbols, incorrect placement of unary/binary operators, unbalanced parentheses, etc.

Usage:
1. Import the required functions from this module.
2. Use the functions as needed in your program.
"""
from operations.operationsFactory import OperationsFactory
from stringManipulation import replaceUnaryMinusesWithUnderscore, signCorrection


def findWrongSymbol(expression: str) -> list:
    """
    Finds wrong symbols in the expression.

    :param expression: The mathematical expression to check.
    :return: List of wrong symbols found in the expression.
    """
    wrong_symbols = []
    factory_instance = OperationsFactory()
    for i in expression:
        if i == '_':
            wrong_symbols.append(i)
        if not i.isnumeric() and not factory_instance.isExists(i) and i != '.':
            wrong_symbols.append(i)

    return wrong_symbols


def findWrongBinaryPlaceSymbol(expression: str) -> list:
    """
    Finds wrong binary placement symbols in the expression.

    :param expression: The mathematical expression to check.
    :return: List of wrong binary placement symbols found in the expression.
    """
    wrong_symbols = []
    exp = signCorrection(expression)
    exp = replaceUnaryMinusesWithUnderscore(exp)
    legit_right_symbols = ['#', '!']
    legit_left_symbols = ['_', '~']
    binary_symbols = ['+', '-', '*', '/', '^', '%', '@', '$', '&']
    for i in range(len(exp) - 1):
        if i != 0:
            if (exp[i] in binary_symbols
                    and (not exp[i - 1].isnumeric() and not exp[i - 1] in legit_right_symbols and
                         exp[i - 1] != ')')):
                wrong_symbols.append(exp[i])

            elif (exp[i] in binary_symbols
                  and (not exp[i + 1].isnumeric() and not exp[i + 1] in legit_left_symbols and
                       exp[i + 1] != '(')):
                wrong_symbols.append(exp[i])
    return wrong_symbols


def findWrongUnaryRightPlaceSymbol(expression: str):
    """
    Finds wrong unary right placement symbols in the expression.

    :param expression: The mathematical expression to check.
    :return: List of wrong unary right placement symbols found in the expression.
    """
    wrong_symbols = []
    legit_right_symbols = ['#', '!']
    binary_symbols = ['+', '-', '*', '/', '^', '%', '@', '$', '&']
    for i in range(len(expression)-1):
        if i != 0:

            if (expression[i] in legit_right_symbols
                    and (not expression[i - 1].isnumeric() and not expression[i - 1] in legit_right_symbols and
                         expression[i - 1] != ')')):
                wrong_symbols.append(expression[i])

            elif (expression[i] in legit_right_symbols
                  and (not expression[i + 1] in binary_symbols and not expression[i + 1] in legit_right_symbols and
                       expression[i + 1] != '(')):
                wrong_symbols.append(expression[i])
    return wrong_symbols


def findWrongUnaryLeftPlaceSymbol(expression: str) -> list:
    """
    Finds wrong unary left placement symbols in the expression.

    :param expression: The mathematical expression to check.
    :return: List of wrong unary left placement symbols found in the expression.
    """
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


def countParenthesis(expression: str) -> bool:
    """
    Counts the number of parentheses in the expression and checks if they are balanced.

    :param expression: The mathematical expression to check.
    :return: True if parentheses are balanced, False otherwise.
    """
    counter = 0
    for i in expression:
        if i == '(':
            counter += 1
        elif i == ')':
            counter -= 1
            if counter < 0:
                return False

    return counter == 0


def nearParenthesis(expression: str) -> bool:
    """
    Checks if parentheses in the expression are placed correctly.

    :param expression: The mathematical expression to check.
    :return: True if parentheses are correctly placed, False otherwise.
    """
    for i in range(len(expression) - 1):
        if i != 0:
            if expression[i] == '(' and (expression[i - 1].isnumeric() or expression[i - 1] == ")"):
                return False
            elif expression[i] == ')' and (expression[i + 1].isnumeric() or expression[i + 1] == '('):
                return False
    return True


def emptyParenthesis(expression: str) -> bool:
    """
    Checks if there are empty parentheses in the expression.

    :param expression: The mathematical expression to check.
    :return: True if there are no empty parentheses, False otherwise.
    """
    for i in range(len(expression)):
        if expression[i] == '(' and expression[i + 1] == ')':
            return False
    return True


def canNotBeInEdges(expression: str) -> list:
    """
    Checks if certain symbols cannot be at the edges of the expression.

    :param expression: The mathematical expression to check.
    :return: List of symbols that cannot be at the edges.
    """
    wrong_symbols = []
    legit_right_edge = ['-', '~', '(']
    legit_left_edge = [')', '!', '#']
    if expression[0] not in legit_right_edge and not expression[0].isnumeric():
        wrong_symbols.append(expression[0])
    elif expression[-1] not in legit_left_edge and not expression[-1].isnumeric():
        wrong_symbols.append(expression[-1])

    return wrong_symbols


def validate_exp(exp: str):
    """
    Validates a mathematical expression for correctness.

    :param exp: The mathematical expression to validate.
    :raises ValueError: If the expression is empty or contains invalid characters.
    :raises SyntaxError: If there are issues with binary/unary operator placement, parentheses balance, or other syntax errors.
    """
    if len(exp) == 0:
        raise ValueError(f'exp is empty ')

    invalid_chars = findWrongSymbol(exp)
    if len(invalid_chars) != 0:
        raise ValueError(f'{invalid_chars}  Unacceptable Symbol ')

    invalid_chars = canNotBeInEdges(exp)
    if len(invalid_chars) != 0:
        raise SyntaxError(f'{invalid_chars}  can not be in edge')

    invalid_chars = findWrongUnaryRightPlaceSymbol(exp)
    if len(invalid_chars) != 0:
        raise SyntaxError(f'{invalid_chars}  Wrong Unary Right Place ')

    invalid_chars = findWrongBinaryPlaceSymbol(exp)
    if len(invalid_chars) != 0:
        raise SyntaxError(f'{invalid_chars}  Wrong Binary Place ')

    invalid_chars = findWrongUnaryLeftPlaceSymbol(exp)
    if len(invalid_chars) != 0:
        raise SyntaxError(f'{invalid_chars}  Wrong Unary Left Place ')

    if not countParenthesis(exp):
        raise SyntaxError('parenthesis are not balanced ')

    if not nearParenthesis(exp):
        raise SyntaxError('parenthesis are not in place ')

    if not emptyParenthesis(exp):
        raise SyntaxError('empty parenthesis ')
