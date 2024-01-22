from operations.operation import Operation


class UnaryOperation(Operation):

    def priority(self) -> int:
        """

        :return: Priority level of the unary operation.
        """
        pass

    def perform(self, operand: float) -> float:
        """

        :param operand: The operand on which the unary operation is performed.
        :return: Result of the unary operation.
        """
        pass


class RightUnaryOperation(UnaryOperation):

    def priority(self) -> int:
        """

        :return: Priority level of the right unary operation.
        """
        pass

    def perform(self, operand: float) -> float:
        """

        :param operand: The operand on which the right unary operation is performed.
        :return: Result of the right unary operation.
        """
        pass


class SumDigitsOperation(UnaryOperation):

    def priority(self) -> int:
        """

        :return: Priority level of the SumDigits unary operation.
        """
        return 6

    def perform(self, operand: float) -> float:
        """

        :param operand: The operand on which the SumDigits unary operation is performed.
        :return: Result of the SumDigits unary operation.
        """
        if operand < 0:
            raise SyntaxError("cannot hash to a negative param")
        if operand == 0:
            return 1
        listo = list(str(operand))
        if 'e' in listo:
            return sum(float(listo[num]) for num in range(listo.index('e')) if listo[num].isnumeric())
        return sum(float(num) for num in listo if num.isnumeric())


class FactorialOperation(RightUnaryOperation):

    def priority(self) -> int:
        """

        :return: Priority level of the factorial right unary operation.
        """
        return 6

    def perform(self, operand: int) -> int:
        """

        :param operand: The operand on which the factorial right unary operation is performed.
        :return: Result of the factorial right unary operation.
        :raises ValueError: If the operand is not a non-negative integer.
        """
        if int(operand) != operand or operand < 0:
            raise ValueError(f"{operand} must be a non-negative integer to compute factorial")
        if operand == 0:
            return 1
        return factorial(operand)


def factorial(n: float):
    result = 1
    for i in range(1, int(n) + 1):
        result *= i
    return result


class LeftUnaryOperation(UnaryOperation):

    def priority(self) -> int:
        """

        :return: Priority level of the left unary operation.
        """
        pass

    def perform(self, operand: float) -> float:
        """

        :param operand: The operand on which the left unary operation is performed.
        :return: Result of the left unary operation.
        """
        pass


class NegativeOperation(LeftUnaryOperation):

    def priority(self) -> int:
        """

        :return: Priority level of the negative left unary operation.
        """
        return 6

    def perform(self, operand: int) -> int:
        """

        :param operand: The operand on which the negative left unary operation is performed.
        :return: Result of the negative left unary operation.
        """
        return -operand


class UnaryMinusOperation(LeftUnaryOperation):

    def priority(self) -> float:
        """

        :return: Priority level of the unary minus left unary operation.
        """

        return 3.5

    def perform(self, operand: int) -> int:
        """

        :param operand: The operand on which the unary minus left unary operation is performed.
        :return: Result of the unary minus left unary operation.
        """
        return -operand


class UnaryMaxMinusOperation(LeftUnaryOperation):

    def priority(self) -> float:
        """

        :return: Priority level of the unary minus left unary operation.
        """

        return 7

    def perform(self, operand: int) -> int:
        """

        :param operand: The operand on which the unary minus left unary operation is performed.
        :return: Result of the unary minus left unary operation.
        """
        return -operand
