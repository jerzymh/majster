from logging import exception
from BandCompressorBase import BandCompressorBase
import matlab.engine

class G7231BasicCompressor(BandCompressorBase):
    def __init__(self, engine) -> None:
        if not isinstance(engine, matlab.engine.matlabengine.MatlabEngine):
            raise Exception("Engine is not matlab engine, but it should be!")
        self.engine = engine

        #self.inputFileName = "G7231basic_compr_input.wav"
        self.outputFileName = "G7231basic_compr_ouput.dat"
        self.reconstuctionFileName = "G7231basic_compr_recnst.wav"
        #self.samplongFreq = samplingFreq
        super().__init__()

    def compress(self, signalFileName):
        #signal = matlab.double(signal)
        #self.engine.wavwrite(signal, self.samplongFreq, self.inputFileName, nargout=0)
        self.engine.G7231Coder_basic(signalFileName, self.outputFileName, nargout=0)
        return self.outputFileName

    def decompress(self, compressedSignalFileName):
        self.engine.G7231Decoder_3(compressedSignalFileName, self.reconstuctionFileName, nargout=0)
        return self.reconstuctionFileName

    def __repr__(self):
        return "G7231BasicCompressor"