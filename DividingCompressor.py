from CompressorBase import CompressorBase

class DividingCompressor(CompressorBase):
    def __init__(self, divider, enhancer, compressors) -> None:
        self.divider = divider
        self.enhancer = enhancer
        self.compressors = compressors
        
    def compress(self, signal):
        enhanced = self.enhancer.enhance(signal)
        divided = self.divider.divide(enhanced)
        compressed = []
        i=0
        for band in divided:
            compressedBand = self.compressors[i].compress(band)
            compressed.append(compressedBand)
            i+=1
        return compressed

    def decompress(self, compressed):
        decompressed = []
        i=0
        for compressedBand in compressed:
            decompressedBand = self.compressors[i].decompress(compressedBand)
            decompressed.append(decompressedBand)
            i+=1
        merged = self.divider.merge(decompressed)
        unenhanced = self.enhancer.unenhance(merged)
        return unenhanced

    def __repr__(self):
        name = "DividingCompressor:(divider:%s)(enhancer:%s)(bandCompressors:%s)"%(self.divider, self.enhancer, self.compressors)
        return name
        