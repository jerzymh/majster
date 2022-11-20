from BandCompressorBase import BandCompressorBase

class DummyCompressor(BandCompressorBase):
    def compress(self, signal):
        return signal
    def decompress(self, signal):
        return signal
    def __repr__(self):
        return "DummyCompressor"