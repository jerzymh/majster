class BandCompressorBase:
    def compress(self, signal):
        raise NotImplementedError
    def decompress(self, signal):
        raise NotImplementedError
    def __repr__(self):
        raise NotImplementedError
    pass