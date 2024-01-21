from operations.operation import Operation


class BinaryOperation(Operation):
    def priority(self) -> int:
        pass

    def perform(self, operand1: float, operand2: float) -> float:
        pass


class AdditionOperation(BinaryOperation):
    def priority(self) -> int:
        return 1

    """Add two numbers."""

    def perform(self, operand1: float, operand2: float) -> float:
        return operand1 + operand2


class AverageOperation(BinaryOperation):
    def priority(self) -> int:
        return 5

    """Calculate the average of two numbers."""

    def perform(self, operand1: float, operand2: float) -> float:
        return (operand1 + operand2) / 2


class DivisionOperation(BinaryOperation):
    def priority(self) -> int:
        return 2

    """Divide num1 by num2, handling division by zero."""

    def perform(self, operand1: float, operand2: float) -> float:
        if operand2 != 0:
            return operand1 / operand2
        else:
            raise ZeroDivisionError("Cannot divide by zero.")


class MaximumOperation(BinaryOperation):
    def priority(self) -> int:
        return 5

    """Return the maximum of two numbers."""

    def perform(self, operand1: float, operand2: float) -> float:

        if operand1 > operand2:
            return operand1
        else:
            return operand2


class MinimumOperation(BinaryOperation):
    def priority(self) -> int:
        return 5

    """Return the minimum of two numbers."""

    def perform(self, operand1: float, operand2: float) -> float:

        if operand1 > operand2:
            return operand2
        else:
            return operand1


class ModuloOperation(BinaryOperation):
    def priority(self) -> int:
        return 4

    """Calculate the modulus of num1 by num2."""

    def perform(self, operand1: float, operand2: float) -> float:
        return operand1 % operand2


class MultiplyOperation(BinaryOperation):
    def priority(self) -> int:
        return 2

    """Multiply two numbers."""

    def perform(self, operand1: float, operand2: float) -> float:
        return operand1 * operand2


class PowerOperation(BinaryOperation):
    def priority(self) -> int:
        return 3

    """Raise num1 to the power of num2."""

    def perform(self, operand1: float, operand2: float) -> float:
        if operand1 > 0 or not 0 < operand2 < 1:
            return pow(operand1, operand2)
        else:
            raise ValueError("Complex Number ")


class SubtractionOperation(BinaryOperation):
    def priority(self) -> int:
        return 1

    """Subtract num2 from num1."""

    def perform(self, operand1: float, operand2: float) -> float:
        return operand1 - operand2
