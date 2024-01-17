from operations.operationsFactory import OperationsFactory


def signCorrection(mathexp: str):
    while '+-' in mathexp or '-+' in mathexp or '++' in mathexp or '--' in mathexp:
        mathexp = mathexp.replace("+-", "-")
        mathexp = mathexp.replace("-+", "-")
        mathexp = mathexp.replace("++", "+")
        mathexp = mathexp.replace("--", "+")
    return mathexp


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


def manipulateString(expression: str):

    expression = signCorrection(expression)
    expression = replaceUnaryMinusesWithUnderscore(expression)
    tokens = splitMathExpression(expression)

    return tokens
