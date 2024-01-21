from helperFunctions import isFloat
from operations.operationsFactory import OperationsFactory
import operations.unaryOperation
from operations.helpOperation import ParenthesisL
from stringManipulation import manipulateString
from validation import validate_exp


def evaluate_expression(exp: str):
    """
    Evaluate a mathematical expression and return the result.

    :param exp: The mathematical expression to be evaluated.
    :return: The result of the evaluation rounded to 3 decimal places.
    """

    values = []
    operators = []
    factory_instance = OperationsFactory()
    validate_exp(exp)
    tokens = manipulateString(exp)
    for token in tokens:
        if token.isnumeric() or isFloat(token):
            values.append(float(token))
        elif token == '(':
            operators.append(factory_instance.getOperation('('))
        elif token == ')':
            while not isinstance(operators[-1], ParenthesisL):
                op = operators.pop()
                if isinstance(op, operations.unaryOperation.UnaryOperation):
                    values.append(op.perform(values.pop()))
                else:
                    num2 = values.pop()
                    num1 = values.pop()
                    values.append(op.perform(num1, num2))

            operators.pop()  # Discard the '('
        elif isinstance(factory_instance.getOperation(token),
                        operations.unaryOperation.LeftUnaryOperation):
            operators.append(OperationsFactory().getOperation(token))

        else:
            op = factory_instance.getOperation(token)
            while operators and op.priority() <= operators[-1].priority():
                op = operators.pop()
                if isinstance(op, operations.unaryOperation.UnaryOperation):
                    values.append(op.perform(values.pop()))
                else:
                    num2 = values.pop()
                    num1 = values.pop()
                    values.append(op.perform(num1, num2))

            operators.append(factory_instance.getOperation(token))

    while len(operators) != 0:
        op = operators.pop()
        if isinstance(op, operations.unaryOperation.UnaryOperation):
            values.append(op.perform(values.pop()))
        else:
            num2 = values.pop()
            num1 = values.pop()
            values.append(op.perform(num1, num2))

    evaluated_num = values.pop()
    return round(evaluated_num, 3)
