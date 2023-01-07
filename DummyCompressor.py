from CompressorBase import CompressorBase

class DummyCompressor(CompressorBase):
    def compress(self, signal):
        return signal
    def decompress(self, signal):
        return signal
    def __repr__(self):
        return "DummyCompressor"