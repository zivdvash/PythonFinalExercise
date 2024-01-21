from operations.binaryOperation import AdditionOperation, SubtractionOperation, MultiplyOperation, DivisionOperation, \
    PowerOperation, ModuloOperation, AverageOperation, MaximumOperation, MinimumOperation
from operations.helpOperation import ParenthesisL, ParenthesisR
from operations.unaryOperation import UnaryMinusOperation, NegativeOperation, FactorialOperation, SumDigitsOperation


class OperationsFactory:
    """

    Singleton class representing a factory for creating different operations.
    """
    _instance = None

    def __new__(cls):
        """

        :return: An instance of the OperationsFactory, creating it if necessary.
        """

        if cls._instance is None:
            cls._instance = super(OperationsFactory, cls).__new__(cls)
            cls._instance.operations = {
                '+': AdditionOperation(),
                '-': SubtractionOperation(),
                '*': MultiplyOperation(),
                '/': DivisionOperation(),
                '^': PowerOperation(),
                '_': UnaryMinusOperation(),
                '%': ModuloOperation(),
                '@': AverageOperation(),
                '$': MaximumOperation(),
                '&': MinimumOperation(),
                '~': NegativeOperation(),
                '!': FactorialOperation(),
                '#': SumDigitsOperation(),
                '(': ParenthesisL(),
                ')': ParenthesisR()
            }
        return cls._instance

    def getOperation(self, operator):
        """

        :param operator: The operator for which an operation is requested.
        :return: The corresponding operation for the given operator.
        :raises ValueError: If the operator is not recognized.
        """
        if operator in self.operations:
            return self.operations.get(operator)
        else:
            raise ValueError(f"Unknown operator: {operator}")

    def isExists(self, operator: str):
        """

        :param operator: The operator to check for existence.
        :return: True if the operator exists in the factory, False otherwise.
        """
        return operator in self.operations
