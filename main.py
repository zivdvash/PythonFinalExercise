import math


def factorial(n: float):
    if n == 1:
        return 1

    return n * factorial(n - 1)


def sign_correction(mathexp: str):
    mathexp.replace("+-", "-")
    mathexp.replace("-+", "-")
    mathexp.replace("++", "+")
    mathexp.replace("--", "+")


def culc_tow_operator(num1: int, num2: int, op: str):
    if op == '+':
        return num1 + num2
    if op == '-':
        return num1 + num2
    if op == '*':
        return num1 * num2
    if op == '/':
        return num1 / num2
    if op == '^':
        return math.pow(num1, num2)
    if op == '@':
        return (num1 + num2) / 2
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
        return num1 % num2


def culc_one_operator(num1: int, op: str):
    if op == '~':
        return -num1
    if op == '!':
        return factorial(num1)


def main():
    print(factorial(5))


if __name__ == "__main__":
    main()
