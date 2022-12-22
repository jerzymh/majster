from DividingCompressorFactory import DividingCompressorFactory
from CompressionQualityMeasurerComposite import CompressionQualityMeasurerComposite
from PEAQCompressionQualityMeasurer import PEAQCompressionQualityMeasurer
from PESQCompressionQualityMeasurer import PESQCompressionQualityMeasurer

factory = DividingCompressorFactory()
dividingCompressors = factory.getCompressors()
audioFilesToTest = ['parole16.WAV', 'probka_audiobook.wav', 'probka_rap.wav', 'probka_sciezka_z_filmu.wav']
measurer = CompressionQualityMeasurerComposite()
measurer.register(PEAQCompressionQualityMeasurer(factory.mlEngine))
measurer.register(PESQCompressionQualityMeasurer())

def TestCompressorsForAudioFile(audioFileToTest, resultsTextFile):
    print("Testing for audio file: '%s'"%audioFileToTest)
    measures = {}
    with open(resultsTextFile, 'a') as resultsFile:
        resultsFile.write(audioFileToTest + '\n')


    for compressor in dividingCompressors:
        try:
            compressed = compressor.compress(audioFileToTest)
            decompressed=compressor.decompress(compressed)
            measure = measurer.measure(audioFileToTest, decompressed)  
        except Exception:
            measure = 'error'
        measures[str(compressor)] = measure
        with open(resultsTextFile, 'a') as resultsFile:
            resultsFile.write(str(compressor)+str(measure)+'\n')

    print(measures)
    return measures

results = []

for audioFileToTest in audioFilesToTest:
    TestCompressorsForAudioFile(audioFileToTest, 'results.txt')



