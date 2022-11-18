class CompressionQualityMeasurerBase:
    def measure(self, originalSignal, reconstruction):
        raise NotImplementedError
    pass