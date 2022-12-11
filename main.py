from DividingCompressorFactory import DividingCompressorFactory
from CompressionQualityMeasurerComposite import CompressionQualityMeasurerComposite
from PEAQCompressionQualityMeasurer import PEAQCompressionQualityMeasurer
from PESQCompressionQualityMeasurer import PESQCompressionQualityMeasurer

factory = DividingCompressorFactory()
dividingCompressors = factory.generate()
audioFilesToTest = ['parole16.WAV', 'probka_audiobook.wav', 'probka_rap.wav', 'probka_sciezka_z_filmu.wav']
measurer = CompressionQualityMeasurerComposite()
measurer.register(PEAQCompressionQualityMeasurer(factory.mlEngine))
measurer.register(PESQCompressionQualityMeasurer())

def TestCompressorsForAudioFile(audioFileToTest):
    print("Testing for audio file: '%s'"%audioFileToTest)

    decompressedByCompressorName = {}

    for compressor in dividingCompressors:
        compressed = compressor.compress(audioFileToTest)
        decompressedByCompressorName[str(compressor)]=compressor.decompress(compressed)
       
    measures = {}
    for compressorName in decompressedByCompressorName:
        measures[(compressorName, measurer)] = measurer.measure(audioFileToTest, decompressedByCompressorName[compressorName])

    print(measures)
    return measures


results = []

for audioFileToTest in audioFilesToTest:
    results.append(TestCompressorsForAudioFile(audioFileToTest))

print('Results:\n', results)


