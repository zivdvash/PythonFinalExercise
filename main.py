import math


def factorial(n: float):
    if n == 1:
        return 1

    return n * factorial(n - 1)


def is_op_Unary(op: str):
    one_operators = ['!', '~']
    if op in one_operators:
        return True
    return False


def sign_correction(mathexp: str):
    while '+-' in mathexp or '-+' in mathexp or '++' in mathexp or '--' in mathexp:
        mathexp = mathexp.replace("+-", "-")
        mathexp = mathexp.replace("-+", "-")
        mathexp = mathexp.replace("++", "+")
        mathexp = mathexp.replace("--", "+")
    return mathexp


def get_operator_precedence(op: str):
    operators = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "@": 5, "$": 5, "&": 5, "~": 6, "!": 6}
    if op in operators:
        return operators.get(op)
    else:
        return -1


def is_float(token):
    try:
        float(token)
        return '.' in token
    except ValueError:
        return False


def culc_two_operator(operators, values):
    num1 = values.pop()
    num2 = values.pop()
    op = operators.pop()

    if op == '+':
        return num2 + num1
    if op == '-':
        return num2 - num1
    if op == '*':
        return num2 * num1
    if op == '/':
        return num2 / num1
    if op == '^':
        return math.pow(num2, num1)
    if op == '@':
        return (num2 + num1) / 2
    if op == '$':
        if num1 > num2:
            return num1
        else:
            return num2
    if op == '&':
        if num1 > num2:
            return num2
        else:
            return num1
    if op == '%':
        return num2 % num1


def split_math_expression(expression):
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


def culc_one_operator(operators, values):
    num1 = values.pop()
    op = operators.pop()
    if op == '~':
        return -num1
    if op == '!':
        return factorial(num1)


def evaluate_expression(expression):
    expression = sign_correction(expression)
    tokens = split_math_expression(expression)
    values = []
    operators = []

    for token in tokens:
        if token.isnumeric() or is_float(token):
            values.append(float(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators[-1] != '(':
                if is_op_Unary(operators[-1]):
                    values.append(culc_one_operator(operators, values))
                else:
                    values.append(culc_two_operator(operators, values))

            operators.pop()
        elif get_operator_precedence(token) != -1:
            while (operators and get_operator_precedence(token) != -1 and
                   get_operator_precedence(token) <= get_operator_precedence(operators[-1])):

                if is_op_Unary(operators[-1]):
                    values.append(culc_one_operator(operators, values))
                else:
                    values.append(culc_two_operator(operators, values))

            operators.append(token)

    while len(operators) != 0:

        if is_op_Unary(operators[-1]):
            result = culc_one_operator(operators, values)
        else:
            result = culc_two_operator(operators, values)
        values.append(result)

    return values.pop()


def main():
    print('Enter expression (type "exit" to quit):')
    exp = input()
    result = split_math_expression(exp)
    print(result)
    print(evaluate_expression(exp))


if __name__ == "__main__":
    main()
