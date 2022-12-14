from EnhancerBase import EnhancerBase

class DummyEnhancer(EnhancerBase):
    def enhance(self, signal):
        return signal
    def unenhance(self, signal):
        return signal
    def __repr__(self):
        return "DummyEnhancer"