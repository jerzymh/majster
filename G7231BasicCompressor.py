from logging import exception
import IPartCompressor as I
import matlab.engine

class G7231BasicCompressor(I.IPartCompressor):
    def __init__(self, engine, samplingFreq) -> None:
        self.inputFileName = "G7231basic_compr_input.wav"
        self.outputFileName = "G7231basic_compr_ouput.dat"
        self.reconstuctionFileName = "G7231basic_compr_recnst.wav"
        if isinstance(engine, matlab.engine.matlabengine.MatlabEngine):
            self.engine = engine
            self.samplongFreq = samplingFreq
        else:
            raise Exception("Engine is not matlab engine, but it should be!")
        super().__init__()

    def compress(self, signal):
        signal = matlab.double(signal)
        self.engine.wavwrite(signal, self.samplongFreq, self.inputFileName, nargout=0)
        self.engine.G7231Coder_basic(self.inputFileName, self.outputFileName, nargout=0)
        return self.outputFileName

    def decompress(self, compressedSignal):
        self.engine.G7231Decoder_3(compressedSignal,self.reconstuctionFileName, nargout=0)
        [u, fs] = self.engine.audioread("diaboj.wav", nargout=2)
        return [u, fs]