from operations.operationsFactory import OperationsFactory


def signCorrection(expression: str) -> str:
    """
    Corrects consecutive double minuses in the expression.

    :param expression: The mathematical expression to correct.
    :return: The expression with consecutive double minuses replaced.
    """
    prev = -1
    i = 0
    changble = len(expression) - 1
    while i < changble:
        if i == 0:
            if expression[i] == '-' and expression[i + 1] == '-':
                expression = expression[:i] + expression[i+2:]
                changble -= 2
            else:
                i += 1
                prev += 1
        elif expression[i] == '-' and expression[prev] in "(+@#$%!^&*~/-" and expression[i + 1] == '-':
            expression = expression[:i] + expression[i+2:]
            changble -= 2
        else:
            i += 1
            prev += 1
    return expression


def splitMathExpression(expression):
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
    prev = -1
    i = 0
    changble = len(expression) - 1
    while i < changble:
        if i == 0:
            if expression[i] == '-':
                expression = expression[:i] + '_' + expression[i+1:]

        elif expression[i] == '-' and expression[prev] in "(+@#$%!^&*~/-":
            expression = expression[:i] + '_' + expression[i+1:]

        i += 1
        prev += 1
    return expression


def replaceMinusesUnaryWithUnderscore(expression: str) -> str:
    if len(expression) <= 1:
        return expression

    i = 0
    while i < len(expression) - 1:
        if expression[i] == '_':
            expression = expression[:i] + '-' + expression[i+1:]
        i += 1
    return expression


def manipulateString(expression: str):
    expression = signCorrection(expression)
    expression = replaceUnaryMinusesWithUnderscore(expression)
    tokens = splitMathExpression(expression)

    return tokens
