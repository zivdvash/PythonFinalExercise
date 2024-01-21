from operations.operation import Operation


class BinaryOperation(Operation):
    """

    :param operand1: The first operand of the binary operation.
    :param operand2: The second operand of the binary operation.
    :return: The result of the binary operation.
    """

    def priority(self) -> int:
        pass

    def perform(self, operand1: float, operand2: float) -> float:
        pass


class AdditionOperation(BinaryOperation):
    def priority(self) -> int:
        """

        :return: Priority level of 1 for addition operation.
        """
        return 1

    def perform(self, operand1: float, operand2: float) -> float:
        """

           :param operand1: The first operand of addition.
           :param operand2: The second operand of addition.
           :return: The sum of operand1 and operand2.
           """
        return operand1 + operand2


class AverageOperation(BinaryOperation):
    def priority(self) -> int:
        """

        :return: Priority level of 5 for average operation.
        """

        return 5

    def perform(self, operand1: float, operand2: float) -> float:
        """

        :param operand1: The first operand for calculating the average.
        :param operand2: The second operand for calculating the average.
        :return: The average of operand1 and operand2.
        """
        return (operand1 + operand2) / 2


class DivisionOperation(BinaryOperation):
    def priority(self) -> int:
        """

        :return: Priority level of 2 for division operation.
        """

        return 2

    def perform(self, operand1: float, operand2: float) -> float:
        """

        :param operand1: The numerator in the division operation.
        :param operand2: The denominator in the division operation.
        :return: The result of dividing operand1 by operand2.
        :raises ZeroDivisionError: If operand2 is zero.
        """
        if operand2 != 0:
            return operand1 / operand2
        else:
            raise ZeroDivisionError("Cannot divide by zero.")


class MaximumOperation(BinaryOperation):
    """

    :return: Priority level of 5 for maximum operation.
    """

    def priority(self) -> int:
        return 5

    def perform(self, operand1: float, operand2: float) -> float:
        """

        :param operand1: The first operand for finding the maximum.
        :param operand2: The second operand for finding the maximum.
        :return: The maximum value between operand1 and operand2.
        """

        if operand1 > operand2:
            return operand1
        else:
            return operand2


class MinimumOperation(BinaryOperation):
    """

    :return: Priority level of 5 for minimum operation.
    """

    def priority(self) -> int:
        return 5

    def perform(self, operand1: float, operand2: float) -> float:
        """

        :param operand1: The first operand for finding the minimum.
        :param operand2: The second operand for finding the minimum.
        :return: The minimum value between operand1 and operand2.
        """

        if operand1 > operand2:
            return operand2
        else:
            return operand1


class ModuloOperation(BinaryOperation):
    """

    :return: Priority level of 4 for modulo operation.
    """

    def priority(self) -> int:
        return 4

    def perform(self, operand1: float, operand2: float) -> float:
        """

        :param operand1: The dividend in the modulo operation.
        :param operand2: The divisor in the modulo operation.
        :return: The remainder of operand1 divided by operand2.
        """
        return operand1 % operand2


class MultiplyOperation(BinaryOperation):
    def priority(self) -> int:
        """

        :return: Priority level of 2 for multiplication operation.
        """

        return 2

    def perform(self, operand1: float, operand2: float) -> float:
        """

        :param operand1: The first operand of multiplication.
        :param operand2: The second operand of multiplication.
        :return: The product of operand1 and operand2.
        """

        return operand1 * operand2


class PowerOperation(BinaryOperation):
    """

    :return: Priority level of 3 for power operation.
    :raises ValueError: If the result is a complex number.
    """

    def priority(self) -> int:
        return 3

    def perform(self, operand1: float, operand2: float) -> float:
        """

        :param operand1: The base in the power operation.
        :param operand2: The exponent in the power operation.
        :return: The result of raising operand1 to the power of operand2.
        :raises ValueError: If operand1 is less than or equal to 0 and operand2 is a multiple of 10.
        """
        if operand1 > 0 or not operand2 % 10 == 0:
            return pow(operand1, operand2)
        else:
            raise ValueError("Complex Number ")


class SubtractionOperation(BinaryOperation):
    def priority(self) -> int:
        """

        :return: Priority level of 1 for subtraction operation.
        """

        return 1

    def perform(self, operand1: float, operand2: float) -> float:
        """

        :param operand1: The minuend in the subtraction operation.
        :param operand2: The subtrahend in the subtraction operation.
        :return: The result of subtracting operand2 from operand1.
        """
        return operand1 - operand2
