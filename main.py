from bz2 import compress
import numpy as np
import matlab.engine
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

factory = DividingCompressorFactory()
dividingCompressors = factory.generate()
decompressed = {}

for compressor in dividingCompressors:
    compressed = compressor.compress('DIABOJ.WAV')
    #decompressed.append(compressor.decompress(compressed))
    decompressed["dummy"]=compressor.decompress(compressed)
    

print(decompressed)