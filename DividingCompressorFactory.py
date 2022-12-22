from DividingCompressor import DividingCompressor
from DummyCompressor import DummyCompressor
from HighbandBooster import HighbandBooster
from G7231Compressor import G7231Compressor
from DummyEnhancer import DummyEnhancer

from QMFDivider import QMFDivider
from QMFWithHighbandModDivider import QMFWithHighbandModDivider

import matlab.engine

class AssemblyPosition:
    def __init__(self, name, possibleAssembliesList) -> None:
        self.name = name
        self.nextPosition = None
        self.possibleAssembliesList = possibleAssembliesList
        self.currentIndex = 0
        pass
    def connectNextPosition(self, position):
        if self.nextPosition == None:
            self.nextPosition = position
        else:
            self.nextPosition.connectNextPosition(position)

    def moveToNext(self):
        if self.currentIndex + 1 < len(self.possibleAssembliesList):
            self.currentIndex += 1
        elif self.nextPosition != None:
            self.currentIndex = 0
            self.nextPosition.moveToNext()
        else:
            raise IndexError()

    
    def getCurrentPositions(self):
        if self.nextPosition == None:
            return [self.possibleAssembliesList[self.currentIndex]]
        else:
            return self.nextPosition.getCurrentPositions() + [self.possibleAssembliesList[self.currentIndex]]

    def hasNextPosition(self):
        if self.currentIndex + 1 < len(self.possibleAssembliesList):
            return True
        elif self.nextPosition != None:
            return self.nextPosition.hasNextPosition()
        else:
            return False
            

class AssemblyCombiner:
    def __init__(self, possibleAssembliesListsByName) -> None:
        self.possibleAssembliesListsByName = possibleAssembliesListsByName
        self.connectPositions()
        pass

    def connectPositions(self) -> None:
        self.firstAssembly = None
        for name in self.possibleAssembliesListsByName:
            newAssemblyPosition = AssemblyPosition(name, self.possibleAssembliesListsByName[name])
            if self.firstAssembly == None:
                self.firstAssembly = newAssemblyPosition
            else:
                self.firstAssembly.connectNextPosition(newAssemblyPosition)

    def hasNextCombination(self):
        return self.firstAssembly.hasNextPosition()

class DividingCompressorFactory:
    def __init__(self):
        self.mlEngine = matlab.engine.start_matlab()
        pass

    def getG7231ListsPair(self):
        G7231Compressors = []
        G7231Compressor1 = G7231Compressor(self.mlEngine)
        G7231Compressors.append(G7231Compressor1)

        G7231Compressor1 = G7231Compressor1.getCopy()
        G7231Compressor1.isUsingCustomImpulseNumber = True
        G7231Compressor1.impulseNumber = 8
        G7231Compressors.append(G7231Compressor1)

        G7231Compressor1 = G7231Compressor1.getCopy()
        G7231Compressor1.impulseNumber = 16
        G7231Compressors.append(G7231Compressor1)
        
        G7231Compressor1 = G7231Compressor1.getCopy()
        G7231Compressor1.impulseNumber = 32
        G7231Compressors.append(G7231Compressor1)

        G7231CompressorsWithExc = []
        for c in G7231Compressors:
            copy = c.getCopy()
            copy.isUsingSeparateExcitation = True
            G7231CompressorsWithExc.append(copy)

        G7231Compressors += G7231CompressorsWithExc

        result = [[],[]]
        for c0 in G7231Compressors:
            c0.outputFileName = "lowbandComp.dat"
            c0.reconstuctionFileName = "lowbandRec.wav"
            c1 = c0.getCopy()
            c1.outputFileName = "highbandComp.dat"
            c1.reconstuctionFileName = "highbandRec.wav"
            result[0].append(c0)
            result[1].append(c1)

        return result


    def getCompressors(self):
        generatedCompressors = []
        dividers = [QMFDivider(self.mlEngine), QMFWithHighbandModDivider(self.mlEngine)]
        enhancers = [DummyEnhancer(), HighbandBooster(self.mlEngine, 10), HighbandBooster(self.mlEngine, 20), HighbandBooster(self.mlEngine, 30)]
        compressorListsPair = self.getG7231ListsPair()
        compressorListsPair[0].append(DummyCompressor())
        compressorListsPair[1].append(DummyCompressor())


        combiner = AssemblyCombiner(
            {
                "highBandCompressor" : compressorListsPair[1],
                "lowBandCompressor" : compressorListsPair[0],
                "enhancer" : enhancers,
                "divider" : dividers
            }
        )

        
        combination = combiner.firstAssembly.getCurrentPositions()
        generatedCompressors.append(DividingCompressor(combination[0], combination[1], [combination[2], combination[3]]))
        while combiner.hasNextCombination():
            combiner.firstAssembly.moveToNext()
            combination = combiner.firstAssembly.getCurrentPositions()
            generatedCompressors.append(DividingCompressor(combination[0], combination[1], [combination[2], combination[3]]))

        return generatedCompressors