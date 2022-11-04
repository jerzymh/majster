from IDivider import IDivider
import matlab.engine

class FirDivider(IDivider.IDivider):
    def __init__(self, filterCoeffsCount):
        self.filterCoeffsCount = filterCoeffsCount
        self.eng = matlab.engine.start_matlab()
        self.filterCoeffs = self.eng.fir1(self.filterCoeffsCount, 0.48, "high")

    def Divide(self, signal):
        self.eng
        return super().Divide()

