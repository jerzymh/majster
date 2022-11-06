from IBandCompressor import IBandCompressor

class DividingCompressorBase(IBandCompressor):
    def __init__(self, divider, enhancer, compressors) -> None:
        self.divider = divider
        self.enhancer = enhancer
        self.compressors = compressors
        
    pass