class DividerBase:
    def divide(self, signal):
        raise NotImplementedError
    def merge(self, factor1, factor2):
        raise NotImplementedError
    def merge(self, factors):
        raise NotImplementedError
    def __repr__(self):
        raise NotImplementedError

    pass