from logging import exception
from CompressorBase import CompressorBase
import matlab.engine

class G7231Compressor(CompressorBase):
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
        if self.isUsingSeparateExcitation:
            self.engine.G7231Coder_mp(signalFileName, self.outputFileName, self.impulseNumber, nargout=0)

        elif self.isUsingCustomImpulseNumber:
            self.engine.G7231Coder_imp(signalFileName, self.outputFileName, self.impulseNumber, nargout=0)

        else:
            self.engine.G7231Coder_basic(signalFileName, self.outputFileName, nargout=0)

        return self.outputFileName

    def decompress(self, compressedSignalFileName):
        self.engine.G7231Decoder_3(compressedSignalFileName, self.reconstuctionFileName, nargout=0)
        return self.reconstuctionFileName

    def __repr__(self):
        result = "G7231Compressor%dImps"%self.impulseNumber
        if self.isUsingSeparateExcitation:
            result += "SepExc"
        return result

    def getCopy(self):
        copy = G7231Compressor(self.engine)
        copy.impulseNumber = self.impulseNumber
        copy.isUsingCustomImpulseNumber = self.isUsingCustomImpulseNumber
        copy.impulseNumber = self.impulseNumber
        copy.isUsingSeparateExcitation = self.isUsingSeparateExcitation
        copy.outputFileName = self.outputFileName
        copy.reconstuctionFileName = self.reconstuctionFileName
        return copy
