from DividingCompressor import DividingCompressor
from DummyCompressor import DummyCompressor
from DummyDivider import DummyDivider
from DummyEncancer import DummyEnhancer

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
    def getNextPositions(self):
        None

    def getCuttentPositions(self):
        None
    
    def hasNextPosition(self):
        None

class AssemblyCombiner:
    def __init__(self, possibleAssembliesListsByName) -> None:
        self.possibleAssembliesListsByName
        pass

    def connectPositions(self, possibleAssembliesListsByName) -> None:
        possibleAssembliesListsByName = {}
        self.firstAssembly = None
        for name in possibleAssembliesListsByName:
            newAssemblyPosition = AssemblyPosition(name, possibleAssembliesListsByName[name])
            if self.firstAssembly == None:
                self.firstAssembly = newAssemblyPosition
            else:
                self.firstAssembly.connectNextPosition(newAssemblyPosition)

class DividingCompressorFactory:
    def __init__(self):
        pass
    def generate(self):
        compressors = []
        dummyDivider = DummyDivider()
        dummyCompressorsList = [DummyCompressor(), DummyCompressor()]
        dummyEnhancer = DummyEnhancer()
        compressors.append(DividingCompressor(dummyDivider, dummyEnhancer, dummyCompressorsList))
        return compressors