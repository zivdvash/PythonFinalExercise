from operations.operation import Operation


class HelpOperation(Operation):
    """

    Base class representing a generic operation.
    """

    def priority(self) -> int:
        """

        :return: Priority level of the HelpOperation.
        """
        pass

    def preform(self, *operands: float) -> float:
        """

        :param operands: Variable number of operands.
        :return: Placeholder method for HelpOperation.
        """
        pass


class ParenthesisL(HelpOperation):
    """

    Class representing a left parenthesis operation.
    """

    def priority(self) -> int:
        """

        :return: Priority level of 0 for ParenthesisL operation.
        """
        return 0

    def preform(self, *operands: float) -> float:
        """

        :param operands: Variable number of operands.
        :return: Placeholder method for ParenthesisL operation.
        """
        pass


class ParenthesisR(HelpOperation):
    """

    Class representing a right parenthesis operation.
    """

    def priority(self) -> int:
        """

        :return: Priority level of 0 for ParenthesisR operation.
        """
        return 0

    def preform(self, *operands: float) -> float:
        """

        :param operands: Variable number of operands.
        :return: Placeholder method for ParenthesisR operation.
        """

        pass
