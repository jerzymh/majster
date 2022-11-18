from IEnhancer import IEnhancer

class DummyEnhancer(IEnhancer):
    def enhance(self, signal):
        return signal
    def unenhance(self, signal):
        return signal