class IBandCompressor:
    def compress(self, signal):
        raise NotImplementedError
    def decompress(self, signal):
        raise NotImplementedError
    pass