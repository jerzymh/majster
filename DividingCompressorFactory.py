from DividingCompressorBase import DividingCompressorBase
from DummyCompressor import DummmyCompressor, DummyCompressor
from DummyDivider import DummyDivider
from DummyEncancer import DummyEnhancer

class DividingCompressorFactory:
    def __init__(self):
        pass
    def generate():
        compressors = []
        dummyDivider = DummyDivider()
        dummyCompressorsList = [DummyCompressor()]
        dummyEnhancer = DummyEnhancer()
        compressors.append(DividingCompressorBase(dummyDivider, dummyEnhancer, dummyCompressorsList))
        return compressors