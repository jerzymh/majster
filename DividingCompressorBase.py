from IBandCompressor import IBandCompressor

class DividingCompressorBase(IBandCompressor):
    def __init__(self, divider, compressors) -> None:
        self.divider = divider
        self.compressors = compressors
        
    pass