from bz2 import compress
# from G7231BasicCompressor import G7231BasicCompressor

# mlEng = matlab.engine.start_matlab()
# [u, fs] = mlEng.audioread("diaboj.wav", nargout=2)
# u = np.array(u)
# u = u[:, 0]
# print(u[0])

# compressor = G7231BasicCompressor(mlEng, fs)
# compressed = compressor.compress(u)
# [reconstruction, fs] = compressor.decompress(compressed)


# mlEng.audiowrite("output.wav", matlab.double(u), fs, nargout=0)

from DividingCompressorFactory import DividingCompressorFactory
from DummyCompressionQualityMeasurer import DummyCompressionQualityMeasurer

factory = DividingCompressorFactory()
dividingCompressors = factory.generate()
audioFileToTest = 'parole16.WAV'
measurers = [DummyCompressionQualityMeasurer()]

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