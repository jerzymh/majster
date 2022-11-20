from DividerBase import DividerBase

class DummyDivider(DividerBase):
    def divide(self, signal):
        return [signal, []]
    def merge(self, factor1, factor2):
        return factor1
    def merge(self, factors):
        return factors[0]
    def __repr__(self):
        return "DummyDivider"