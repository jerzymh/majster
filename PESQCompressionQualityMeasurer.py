from CompressionQualityMeasurerBase import CompressionQualityMeasurerBase
import subprocess


class PESQCompressionQualityMeasurer(CompressionQualityMeasurerBase):
    def measure(self, originalSignalFileName, reconstructionFileName):
        out = subprocess.Popen(['pesq/pesq', '+16000', '+wb', originalSignalFileName, reconstructionFileName], 
        stdout = subprocess.PIPE, 
        stderr = subprocess.STDOUT)
        stdout, stderr = out.communicate()
        outStr = str(stdout)
        measureResultStr = outStr.split(' ')[-1].replace("\\n","").replace("\\r","").replace("\"","")
        return measureResultStr
        
    def __repr__(self):
        return "PESQCompressionQualityMeasurer"