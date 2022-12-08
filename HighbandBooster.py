from logging import exception
from EnhancerBase import EnhancerBase
import matlab.engine

class HighbandBooster(EnhancerBase):
    def __init__(self, engine, leveldB) -> None:
        if not isinstance(engine, matlab.engine.matlabengine.MatlabEngine):
            raise Exception("Engine is not matlab engine, but it should be!")
        self.engine = engine

        self.leveldB = leveldB
        super().__init__()

    def enhance(self, signalFileName):
        return self.boost(signalFileName, self.leveldB)

    def unenhance(self, signalFileName):
        return self.boost(signalFileName, -self.leveldB)

    def boost(self, inputFileName, leveldB):
        outputFileName = inputFileName + "_" + str(leveldB) + "dB.wav"
        self.engine.HighbandBoost(inputFileName, outputFileName, leveldB, nargout=0)
        return outputFileName

    def __repr__(self):
        return "HighbandBooster" + str(self.level) + "dB"