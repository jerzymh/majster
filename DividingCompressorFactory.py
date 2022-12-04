from DividingCompressor import DividingCompressor
from DummyCompressor import DummyCompressor
from DummyDivider import DummyDivider
from DummyEncancer import DummyEnhancer

from QMFDivider import QMFDivider

import matlab.engine

class DividingCompressorFactory:
    def __init__(self):
        pass
    def generate(self):
        mlEngine = matlab.engine.start_matlab()
        generatedCompressors = []
        # dummyDivider = DummyDivider()
        divider = QMFDivider(mlEngine)

        dummyCompressorsList = [DummyCompressor(), DummyCompressor()]
        dummyEnhancer = DummyEnhancer()
        generatedCompressors.append(DividingCompressor(divider, dummyEnhancer, dummyCompressorsList))
        return generatedCompressors