from DividerBase import DividerBase
import matlab.engine

class FirDivider(DividerBase.DividerBase):
    def __init__(self, filterCoeffsCount):
        self.filterCoeffsCount = filterCoeffsCount
        self.eng = matlab.engine.start_matlab()
        self.filterCoeffs = self.eng.fir1(self.filterCoeffsCount, 0.48, "high")

    def divide(self, signal):
        self.eng
        return super().Divide()

