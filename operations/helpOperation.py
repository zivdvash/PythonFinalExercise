from operations.operation import Operation


class HelpOperation(Operation):
    def priority(self) -> int:
        pass

    def preform(self, *operands: float) -> float:
        pass


class ParenthesisL(HelpOperation):
    def priority(self) -> int:
        return 0

    def preform(self, *operands: float) -> float:
        pass


class ParenthesisR(HelpOperation):
    def priority(self) -> int:
        return 0

    def preform(self, *operands: float) -> float:
        pass
