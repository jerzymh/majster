from IDivider import IDivider

class DummyDivider(IDivider):
    def divide(self, signal):
        return [signal, []]
    def merge(self, factor1, factor2):
        return factor1
    def merge(self, factors):
        return factors[0]