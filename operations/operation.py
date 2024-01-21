class Operation:
    """

    Base class representing a generic operation.
    """

    def priority(self) -> int:
        """

        :return: Priority level of the operation.
        """
        pass

    def preform(self, *operands: float) -> float:
        """

        :param operands: Variable number of operands.
        :return: Placeholder method for the operation.
        """

        pass
