from DividerBase import DividerBase

class DummyDivider(DividerBase):
    def divide(self, signal):
        return [signal, signal]
    def merge(self, factors):
        return factors[0]
    def __repr__(self):
        return "DummyDivider"