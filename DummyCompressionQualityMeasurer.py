from CompressionQualityMeasurerBase import CompressionQualityMeasurerBase

class DummyCompressionQualityMeasurer(CompressionQualityMeasurerBase):
    def measure(self, originalSignal, reconstruction):
        return str('1 dummy unit')
    def __repr__(self):
        return "DummyCompressionQualityMeasurer"