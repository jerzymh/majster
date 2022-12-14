from CompressionQualityMeasurerBase import CompressionQualityMeasurerBase
import matlab.engine


class PEAQCompressionQualityMeasurer(CompressionQualityMeasurerBase):
    def __init__(self, engine) -> None:
        if not isinstance(engine, matlab.engine.matlabengine.MatlabEngine):
            raise Exception("Engine is not matlab engine, but it should be!")
        self.engine = engine
        self.engine.addpath('PEAQ')
        self.engine.addpath('PEAQ\PQevalAudio')
        self.engine.addpath('PEAQ\PQevalAudio\CB')
        self.engine.addpath('PEAQ\PQevalAudio\Misc')
        self.engine.addpath('PEAQ\PQevalAudio\MOV')
        self.engine.addpath('PEAQ\PQevalAudio\Patt')
        super().__init__()

    def measure(self, originalSignalFileName, reconstructionFileName):
        result = self.engine.PEAQMeasure(originalSignalFileName, reconstructionFileName)
        return str(result)
        
    def __repr__(self):
        return "PEAQCompressionQualityMeasurer"