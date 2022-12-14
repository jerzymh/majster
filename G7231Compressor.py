from logging import exception
from BandCompressorBase import BandCompressorBase
import matlab.engine

class G7231Compressor(BandCompressorBase):
    def __init__(self, engine) -> None:
        if not isinstance(engine, matlab.engine.matlabengine.MatlabEngine):
            raise Exception("Engine is not matlab engine, but it should be!")
        self.engine = engine

        #self.inputFileName = "G7231basic_compr_input.wav"
        self.outputFileName = "G7231basic_compr_ouput.dat"
        self.reconstuctionFileName = "G7231basic_compr_recnst.wav"
        self.engine.addpath('G7231new')

        self.isUsingCustomImpulseNumber = False
        self.isUsingSeparateExcitation = False
        self.impulseNumber = 4

        #self.samplongFreq = samplingFreq
        super().__init__()

    def compress(self, signalFileName):
        #signal = matlab.double(signal)
        #self.engine.wavwrite(signal, self.samplongFreq, self.inputFileName, nargout=0)
        if self.isUsingCustomImpulseNumber:
            self.engine.G7231Coder_imp(signalFileName, self.outputFileName, self.impulseNumber, nargout=0)

        elif self.isUsingSeparateExcitation:
            self.engine.G7231Coder_mp(signalFileName, self.outputFileName, self.impulseNumber, nargout=0)

        else:
            self.engine.G7231Coder_basic(signalFileName, self.outputFileName, nargout=0)

        return self.outputFileName

    def decompress(self, compressedSignalFileName):
        self.engine.G7231Decoder_3(compressedSignalFileName, self.reconstuctionFileName, nargout=0)
        return self.reconstuctionFileName

    def __repr__(self):
        return "G7231Compressor"