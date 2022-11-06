from IEnhancer import IEnhancer

class DummyEnhancer(IEnhancer):
    def enhance(self, signal):
        return signal