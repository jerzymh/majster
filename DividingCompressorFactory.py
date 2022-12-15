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
        self.currentIndex = -1
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

    def getNextPositions(self):
        self.moveToNext()
        self.getCurrentPositions()
        None
    
    def getCurrentPositions(self):
        if self.nextPosition == None:
            return [self.possibleAssembliesList[self.currentIndex]]
        else:
            return self.nextPosition.getCurrentPositions.append(self.possibleAssembliesList[self.currentIndex])

    def hasNextPosition(self):
        if self.currentIndex + 1 < len(self.possibleAssembliesList):
            return True
        elif self.nextPosition != None:
            return self.nextPosition.hasNextPosition
        else:
            return False
            

class AssemblyCombiner:
    def __init__(self, possibleAssembliesListsByName) -> None:
        self.possibleAssembliesListsByName
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

    def getNextCombination(self):
        return self.firstAssembly.getNextPositions()

    def hasNextCombination(self):
        return self.firstAssembly.hasNextPosition()

class DividingCompressorFactory:
    def __init__(self):
        self.mlEngine = matlab.engine.start_matlab()
        pass
    def generate(self):
        generatedCompressors = []

        dividers = [QMFDivider(self.mlEngine), QMFWithHighbandModDivider(self.mlEngine)]
        enhancers = [DummyEnhancer(), HighbandBooster()]
        highBandCompressors = [DummyCompressor()]
        lowBandCompressors = [DummyCompressor()]
        
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

        G7231Compressor1 = G7231Compressor1.getCopy()
        G7231Compressor1.impulseNumber = 64
        G7231Compressors.append(G7231Compressor1)

        for c in G7231Compressors:
            copy = c.getCopy()
            copy.isUsingSeparateExcitation = True
            .......................

        # dummyDivider = DummyDivider()
        # divider = QMFWithHighbandModDivider(self.mlEngine)

        bandCompressorsList = [G7231Compressor1, G7231Compressor2]
        highbandBooster = HighbandBooster(self.mlEngine, 10)
        generatedCompressors.append(DividingCompressor(divider, highbandBooster, bandCompressorsList))
        return generatedCompressors