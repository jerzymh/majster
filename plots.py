import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt

class ResultsPlotData:
    def __init__(self, resultsDataFrame, xAxis, yAxes, yAxesDisplayNames) -> None:
        self.resultsDataFrame = resultsDataFrame
        self.xAxis = xAxis
        self.yAxes = yAxes
        self.yAxesDisplayNames = yAxesDisplayNames

class ResultsPlot:
    def __init__(self, plotsData, name, fileName, xAxisName, yAxisName) -> None:
        self.plotsData = plotsData
        self.name = name
        self.fileName = fileName
        self.xAxisName = xAxisName
        self.yAxisName = yAxisName
    def draw(self):
        plt.figure()
        plt.rcParams['font.family'] = ['serif']
        for plotData in self.plotsData:
            ResultsPlot.drawPlotData(plotData)
        plt.grid(True)
        plt.legend(title='Legenda:')
        plt.title(self.name)
        plt.xlabel(self.xAxisName)
        plt.ylabel(self.yAxisName)
        #plt.show()
        plt.savefig(self.fileName, dpi=350)

    def drawPlotData(plotData):
        for yAxis in plotData.yAxes:
            plt.plot(plotData.resultsDataFrame[plotData.xAxis], plotData.resultsDataFrame[yAxis], 'o-', label=plotData.yAxesDisplayNames[yAxis])


results = pd.read_csv('results.csv', encoding='cp1250', delimiter=';')
results = results.assign(PEAQMOS=results["PEAQ"] + 5)


dataFrame = results[  (results["filename"] == "parole16.WAV") 
                    & (results["divider"] == "QMFDivider") 
                    & (results["enhancer"] == "DummyEnhancer")
                    & (results["lowbandCompressor"] == "G7231Compressor")
                    & (results["highbandCompressor"] == "G7231Compressor")
                    & (results["highbandImpulseNumber"] == 4)
                    & (results["lowbandSeparateExcitation"].isnull())
                    & (results["highbandSeparateExcitation"].isnull())]

plotsData = [ ResultsPlotData(dataFrame, 'lowbandImpulseNumber', ['PESQ', 'PEAQMOS'], {'PESQ' : 'PESQ', 'PEAQMOS' : 'PEAQ'}) ]

dataFrame = results[  (results["filename"] == "parole16.WAV") 
                    & (results["divider"] == "QMFDivider") 
                    & (results["enhancer"] == "DummyEnhancer")
                    & (results["lowbandCompressor"] == "G7231Compressor")
                    & (results["highbandCompressor"] == "G7231Compressor")
                    & (results["highbandImpulseNumber"] == 4)
                    & (results["lowbandSeparateExcitation"].notnull())
                    & (results["highbandSeparateExcitation"].notnull())]
                    
plotsData.append( ResultsPlotData(dataFrame, 'lowbandImpulseNumber', ['PESQ', 'PEAQMOS'], {'PESQ' : 'PESQ oddzielne wzbudzenie', 'PEAQMOS' : 'PEAQ oddzielne wzbudzenie'}) )

plot = ResultsPlot(plotsData, 'Wykres zależności oceny jakości\nod liczby impulsów w dolnym paśmie', 'figures/parole16odDolnegoPasma.svg', 'Liczba impulsów', 'Aproksymacja MOS')
plot.draw()

dataFrame = results[  (results["filename"] == "parole16.WAV") 
                    & (results["divider"] == "QMFDivider") 
                    & (results["enhancer"] == "DummyEnhancer")
                    & (results["lowbandCompressor"] == "G7231Compressor")
                    & (results["highbandCompressor"] == "G7231Compressor")
                    & (results["lowbandImpulseNumber"] == 16)
                    & (results["lowbandSeparateExcitation"].isnull())
                    & (results["highbandSeparateExcitation"].isnull())]

plotsData = [ ResultsPlotData(dataFrame, 'highbandImpulseNumber', ['PESQ', 'PEAQMOS'], {'PESQ' : 'PESQ', 'PEAQMOS' : 'PEAQ'}) ]

dataFrame = results[  (results["filename"] == "parole16.WAV") 
                    & (results["divider"] == "QMFDivider") 
                    & (results["enhancer"] == "DummyEnhancer")
                    & (results["lowbandCompressor"] == "G7231Compressor")
                    & (results["highbandCompressor"] == "G7231Compressor")
                    & (results["lowbandImpulseNumber"] == 16)
                    & (results["lowbandSeparateExcitation"].notnull())
                    & (results["highbandSeparateExcitation"].notnull())]
                    
plotsData.append( ResultsPlotData(dataFrame, 'highbandImpulseNumber', ['PESQ', 'PEAQMOS'], {'PESQ' : 'PESQ oddzielne wzbudzenie', 'PEAQMOS' : 'PEAQ oddzielne wzbudzenie'}) )

plot = ResultsPlot(plotsData, 'Wykres zależności oceny jakości\nod liczby impulsów w górnym paśmie', 'figures/parole16odGornegoPasma.svg', 'Liczba impulsów', 'Aproksymacja MOS')
plot.draw()

#print(firstPlot.head())

# for i in firstPlot[:]:
#     print(i)

# plt.plot(firstPlot['lowbandImpulseNumber'], firstPlot['PEAQ']+5, 'o-', label='PEAQ')
# plt.plot(firstPlot['lowbandImpulseNumber'], firstPlot['PESQ'], 'o-', label='PESQ')
# plt.grid(True)
# plt.legend(title='Legenda:')
# #plt.show()
# plt.savefig('figures/img1.svg',dpi=350)

# plt.figure()