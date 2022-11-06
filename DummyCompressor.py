from IBandCompressor import IBandCompressor

class DummmyCompressor(IBandCompressor):
    def compress(self, signal):
        return signal
    def decompress(self, signal):
        return signal