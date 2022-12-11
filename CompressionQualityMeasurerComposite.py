from CompressionQualityMeasurerBase import CompressionQualityMeasurerBase
import subprocess


class CompressionQualityMeasurerComposite(CompressionQualityMeasurerBase):
    def __init__(self) -> None:
        self.measurers = {}
        super().__init__()

    def register(self, name, measurer):
        self.measurers[name] = measurer

    def register(self, measurer):
        self.measurers[str(measurer)] = measurer


    def measure(self, originalSignalFileName, reconstructionFileName):
        measureResults = {}
        for measurer in self.measurers:
            measureResults[measurer] = self.measurers[measurer].measure(originalSignalFileName, reconstructionFileName)
        return str(measureResults)
        
    def __repr__(self):
        result = 'CompressionQualityMeasurerComposite:('
        for measurer in self.measurers:
            result += measurer
            result += ','
        result += ')'
        return result