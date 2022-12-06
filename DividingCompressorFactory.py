from DividingCompressor import DividingCompressor
from DummyCompressor import DummyCompressor
from DummyDivider import DummyDivider
from DummyEncancer import DummyEnhancer
from G7231BasicCompressor import G7231BasicCompressor

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

        g7231basicCompressor1 = G7231BasicCompressor(mlEngine)
        g7231basicCompressor1.outputFileName = 'G7231_1_output.wav'
        g7231basicCompressor1.reconstuctionFileName = 'G7231_1_reconst.wav'
        g7231basicCompressor2 = G7231BasicCompressor(mlEngine)
        g7231basicCompressor2.outputFileName = 'G7231_2_output.wav'
        g7231basicCompressor2.reconstuctionFileName = 'G7231_2_reconst.wav'
        bandCompressorsList = [g7231basicCompressor1, g7231basicCompressor2]
        dummyEnhancer = DummyEnhancer()
        generatedCompressors.append(DividingCompressor(divider, dummyEnhancer, bandCompressorsList))
        return generatedCompressors