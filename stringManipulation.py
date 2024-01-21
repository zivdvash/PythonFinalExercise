"""
Utility functions for manipulating mathematical expressions.

Includes functions for sign correction, splitting math expressions into tokens, and replacing unary minuses with underscores.

Usage:
1. Import the required functions from this module.
2. Use the functions as needed in your program.
"""

from operations.operationsFactory import OperationsFactory


def signCorrection(expression: str) -> str:
    """
    Corrects consecutive double minuses in the expression.

    :param expression: The mathematical expression to correct.
    :return: The expression with consecutive double minuses replaced.
    """
    i = 0
    while i < len(expression) - 3:
        if expression[i] == '-' and expression[i + 1] == '-' and not expression[i + 2].isnumeric():
            expression = expression.replace("--", "")
        i += 1
    return expression


def splitMathExpression(expression: str) -> list:
    """
    Splits a mathematical expression into tokens.

    :param expression: The mathematical expression to split.
    :return: List of tokens in the expression.
    """
    tokens = []
    current_token = ''

    for char in expression:
        if char.isdigit() or char == '.':
            current_token += char
        else:
            if current_token:
                tokens.append(current_token)
                current_token = ''
            if char.strip():
                tokens.append(char)

    if current_token:
        tokens.append(current_token)

    return tokens


def replaceUnaryMinusesWithUnderscore(expression: str) -> str:
    """
    Replaces unary minuses with underscores in the expression.

    :param expression: The mathematical expression to modify.
    :return: The expression with unary minuses replaced with underscores.
    """
    if len(expression) <= 1:
        return expression

    if expression[0] == '-' and (expression[1].isdigit() or expression[1] == '('):
        expression = expression[:0] + '_' + expression[0 + 1:]

    i = 0
    while i < len(expression) - 1:
        if expression[i] == '-':
            right_neighbor = expression[i + 1]
            left_neighbor = expression[i - 1]
            op = OperationsFactory().isExists(left_neighbor)
            if op or left_neighbor == '(' or left_neighbor == ')':
                if right_neighbor.isdigit() or right_neighbor == '(':
                    expression = expression[:i] + '_' + expression[i + 1:]
        i += 1

    return expression


def manipulateString(expression: str) -> list:
    """
    Manipulates a mathematical expression by applying sign correction,
    splitting into tokens, and replacing unary minuses with underscores.

    :param expression: The mathematical expression to manipulate.
    :return: List of tokens in the manipulated expression.
    """
    expression = signCorrection(expression)
    expression = replaceUnaryMinusesWithUnderscore(expression)
    tokens = splitMathExpression(expression)

    return tokens
