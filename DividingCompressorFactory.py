from DividingCompressor import DividingCompressor
from DummyCompressor import DummyCompressor
from DummyDivider import DummyDivider
from HighbandBooster import HighbandBooster
from G7231Compressor import G7231Compressor

from QMFWithHighbandModDivider import QMFWithHighbandModDivider

import matlab.engine

class DividingCompressorFactory:
    def __init__(self):
        self.mlEngine = matlab.engine.start_matlab()
        pass
    def generate(self):
        generatedCompressors = []
        # dummyDivider = DummyDivider()
        divider = QMFWithHighbandModDivider(self.mlEngine)

        G7231Compressor1 = G7231Compressor(self.mlEngine)
        G7231Compressor1.outputFileName = 'G7231_1_output.wav'
        G7231Compressor1.reconstuctionFileName = 'G7231_1_reconst.wav'
        G7231Compressor1.isUsingCustomImpulseNumber = True
        G7231Compressor1.impulseNumber = 8
        G7231Compressor2 = G7231Compressor(self.mlEngine)
        G7231Compressor2.outputFileName = 'G7231_2_output.wav'
        G7231Compressor2.reconstuctionFileName = 'G7231_2_reconst.wav'
        G7231Compressor2.isUsingSeparateExcitation = True
        G7231Compressor2.impulseNumber = 10
        bandCompressorsList = [G7231Compressor1, G7231Compressor2]
        highbandBooster = HighbandBooster(self.mlEngine, 10)
        generatedCompressors.append(DividingCompressor(divider, highbandBooster, bandCompressorsList))
        return generatedCompressors