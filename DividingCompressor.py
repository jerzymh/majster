from IBandCompressor import IBandCompressor

class DividingCompressor(IBandCompressor):
    def __init__(self, divider, enhancer, compressors) -> None:
        self.divider = divider
        self.enhancer = enhancer
        self.compressors = compressors
        
    def compress(self, signal):
        raise NotImplementedError
    def decompress(self, signal):
        raise NotImplementedError
        