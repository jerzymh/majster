from logging import exception
from DividerBase import DividerBase
import matlab.engine

class QMFDivider(DividerBase):
    def __init__(self, engine) -> None:
        if not isinstance(engine, matlab.engine.matlabengine.MatlabEngine):
            raise Exception("Engine is not matlab engine, but it should be!")
        self.engine = engine

        self.lowBandFilename = "low.wav"
        self.highBandFilename = "high.wav"
        self.reconstructionFileName = "merged.wav"

        super().__init__()

    def divide(self, inputFileName):
        self.engine.QMFDivide(inputFileName, self.lowBandFilename, self.highBandFilename, nargout=0)
        return [self.lowBandFilename, self.highBandFilename]

    def merge(self, factors):
        if not len(factors) == 2:
            raise ValueError("There should be 2 factors")
        
        self.engine.QMFMerge(self.reconstructionFileName, factors[0], factors[1], nargout=0)
        return self.reconstructionFileName

    def __repr__(self):
        return "QMFDivider"