from operations.binaryOperation import AdditionOperation, SubtractionOperation, MultiplyOperation, DivisionOperation, \
    PowerOperation, ModuloOperation, AverageOperation, MaximumOperation, MinimumOperation
from operations.helpOperation import ParenthesisL, ParenthesisR
from operations.unaryOperation import UnaryMinusOperation, NegativeOperation, FactorialOperation, SumDigitsOperation


class OperationsFactory:
    _instance = None

    def __new__(cls):
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
        if operator in self.operations:
            return self.operations.get(operator)
        else:
            raise ValueError(f"Unknown operator: {operator}")

    def isExists(self, operator: str):
        return operator in self.operations
