from PEAQCompressionQualityMeasurer import PEAQCompressionQualityMeasurer

import matlab.engine

mlEngine = matlab.engine.start_matlab()
measurer = PEAQCompressionQualityMeasurer(mlEngine)

result = measurer.measure('parole16.wav', 'merged.wav_-10.0dB.wav')

print(str(result))