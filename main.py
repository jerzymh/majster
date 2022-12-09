from DividingCompressorFactory import DividingCompressorFactory
from PESQCompressionQualityMeasurer import PESQCompressionQualityMeasurer

factory = DividingCompressorFactory()
dividingCompressors = factory.generate()
audioFileToTest = 'parole16.WAV'
measurers = [PESQCompressionQualityMeasurer()]

print("Testing for audio file: '%s'"%audioFileToTest)

decompressedByCompressorName = {}

for compressor in dividingCompressors:
    compressed = compressor.compress(audioFileToTest)
    decompressedByCompressorName[str(compressor)]=compressor.decompress(compressed)
    
measures = {}
for compressorName in decompressedByCompressorName:
    for m in measurers:
        measures[(compressorName, m)] = m.measure(audioFileToTest, decompressedByCompressorName[compressorName])
    

print(measures)