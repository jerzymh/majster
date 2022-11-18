from DividingCompressor import DividingCompressor
from DummyCompressor import DummyCompressor
from DummyDivider import DummyDivider
from DummyEncancer import DummyEnhancer

class DividingCompressorFactory:
    def __init__(self):
        pass
    def generate(self):
        compressors = []
        dummyDivider = DummyDivider()
        dummyCompressorsList = [DummyCompressor(), DummyCompressor()]
        dummyEnhancer = DummyEnhancer()
        compressors.append(DividingCompressor(dummyDivider, dummyEnhancer, dummyCompressorsList))
        return compressors