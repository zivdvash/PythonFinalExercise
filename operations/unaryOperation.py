from operations.operation import Operation


class UnaryOperation(Operation):
    def priority(self) -> int:
        pass

    def perform(self, operand: float) -> float:
        pass


class RightUnaryOperation(UnaryOperation):
    def priority(self) -> int:
        pass

    def perform(self, operand: float) -> float:
        pass


class SumDigitsOperation(UnaryOperation):
    def priority(self) -> int:
        return 6

    def perform(self, operand: float) -> float:
        val = str(operand)
        val = val.replace('.', '')
        res = 0
        for digit in val:
            res += int(digit)
        return res


class FactorialOperation(RightUnaryOperation):
    def priority(self) -> int:
        return 6

    def perform(self, operand: int) -> int:
        if int(operand) != operand or operand < 0:
            raise ValueError(f"{operand} must be an integer and above 0 to do factorial")
        if operand == 0:
            return 1
        return factorial(operand)


def factorial(n: float):
    if n == 1:
        return 1

    return n * factorial(n - 1)


class LeftUnaryOperation(UnaryOperation):
    def priority(self) -> int:
        pass

    def perform(self, operand: float) -> float:
        pass


class NegativeOperation(LeftUnaryOperation):
    def priority(self) -> int:
        return 6

    def perform(self, operand: int) -> int:
        return -operand


class UnaryMinusOperation(LeftUnaryOperation):
    def priority(self) -> float:
        return 3.5

    def perform(self, operand: int) -> int:
        return -operand
