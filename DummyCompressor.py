from IBandCompressor import IBandCompressor

class DummyCompressor(IBandCompressor):
    def compress(self, signal):
        return signal
    def decompress(self, signal):
        return signal