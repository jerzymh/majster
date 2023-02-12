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
highbandEnhanceByEnhancerName = {
    'DummyEnhancer' : 0,
    'HighbandBooster10.0dB' : 10,
    'HighbandBooster20.0dB' : 20,
    'HighbandBooster30.0dB' : 30
}
results['highbandEnhance'] = results['enhancer'].map(highbandEnhanceByEnhancerName)

fileNames = results['filename'].unique()

#################################################################################################################################################
#wykres zależności MOS od liczby impulsów w kompresji dolnoprzepustowej z oddzielnym wzbudzeniem i bez

for fileName in fileNames:
    dataFrame = results[  (results["filename"] == fileName) 
                        & (results["divider"] == "QMFDivider") 
                        & (results["enhancer"] == "DummyEnhancer")
                        & (results["lowbandCompressor"] == "G7231Compressor")
                        & (results["highbandCompressor"] == "G7231Compressor")
                        & (results["highbandImpulseNumber"] == 4)
                        & (results["lowbandSeparateExcitation"].isnull())
                        & (results["highbandSeparateExcitation"].isnull())]

    plotsData = [ 
        ResultsPlotData
            (dataFrame, 'lowbandImpulseNumber', ['PESQ', 'PEAQMOS'], 
            {'PESQ' : 'PESQ (wspólne wzbudzenie)', 'PEAQMOS' : 'PEAQ (wspólne wzbudzenie)'}) 
    ]

    dataFrame = results[  (results["filename"] == fileName) 
                        & (results["divider"] == "QMFDivider") 
                        & (results["enhancer"] == "DummyEnhancer")
                        & (results["lowbandCompressor"] == "G7231Compressor")
                        & (results["highbandCompressor"] == "G7231Compressor")
                        & (results["highbandImpulseNumber"] == 4)
                        & (results["lowbandSeparateExcitation"].notnull())
                        & (results["highbandSeparateExcitation"].notnull())]
                        
    plotsData.append( 
        ResultsPlotData(
            dataFrame, 'lowbandImpulseNumber', ['PESQ', 'PEAQMOS'], 
            {'PESQ' : 'PESQ (oddzielne wzbudzenie)', 'PEAQMOS' : 'PEAQ (oddzielne wzbudzenie)'}
        ) 
    )

    plot = ResultsPlot(plotsData, '',#'Zależności aproksymacji MOS od liczby impulsów w dolnym paśmie\n' 
                                    #'G723.1H_Imp=4, plik ' + fileName, 
                                    'figures/' + fileName + 'odDolnegoPasmaWzb.png', 'Liczba impulsów', 'Aproksymacja MOS')
    plot.draw()

#################################################################################################################################################
#wykres zależności MOS od liczby impulsów w kompresji górnoprzepustowej z oddzielnym wzbudzeniem i bez

for fileName in fileNames:
    dataFrame = results[  (results["filename"] == fileName) 
                        & (results["divider"] == "QMFDivider") 
                        & (results["enhancer"] == "DummyEnhancer")
                        & (results["lowbandCompressor"] == "G7231Compressor")
                        & (results["highbandCompressor"] == "G7231Compressor")
                        & (results["lowbandImpulseNumber"] == 16)
                        & (results["lowbandSeparateExcitation"].isnull())
                        & (results["highbandSeparateExcitation"].isnull())]

    plotsData = [ 
        ResultsPlotData(
            dataFrame, 'highbandImpulseNumber', ['PESQ', 'PEAQMOS'], 
            {'PESQ' : 'PESQ (wspólne wzbudzenie)', 'PEAQMOS' : 'PEAQ (wspólne wzbudzenie)'}
        ) 
    ]

    dataFrame = results[  (results["filename"] == fileName) 
                        & (results["divider"] == "QMFDivider") 
                        & (results["enhancer"] == "DummyEnhancer")
                        & (results["lowbandCompressor"] == "G7231Compressor")
                        & (results["highbandCompressor"] == "G7231Compressor")
                        & (results["lowbandImpulseNumber"] == 16)
                        & (results["lowbandSeparateExcitation"].notnull())
                        & (results["highbandSeparateExcitation"].notnull())]
                        
    plotsData.append( 
        ResultsPlotData(
            dataFrame, 'highbandImpulseNumber', ['PESQ', 'PEAQMOS'], 
            {'PESQ' : 'PESQ (oddzielne wzbudzenie)', 'PEAQMOS' : 'PEAQ (oddzielne wzbudzenie)'}
        ) 
    )

    plot = ResultsPlot(plotsData, '', 
                                    'figures/' + fileName + 'odGornegoPasmaWzb.png', 'Liczba impulsów w górnym paśmie', 'Aproksymacja MOS')
    plot.draw()


#################################################################################################################################################
#wykres zależności MOS od liczby impulsów w kompresji dolnoprzepustowej z modyfikacją QMF i bez

for fileName in fileNames:
    dataFrame = results[  (results["filename"] == fileName) 
                        & (results["divider"] == "QMFDivider") 
                        & (results["enhancer"] == "DummyEnhancer")
                        & (results["lowbandCompressor"] == "G7231Compressor")
                        & (results["highbandCompressor"] == "G7231Compressor")
                        & (results["highbandImpulseNumber"] == 4)
                        & (results["lowbandSeparateExcitation"].isnull())
                        & (results["highbandSeparateExcitation"].isnull())]

    plotsData = [ 
        ResultsPlotData
            (dataFrame, 'lowbandImpulseNumber', ['PESQ', 'PEAQMOS'], 
            {'PESQ' : 'PESQ (bez modyfikacji widma)', 'PEAQMOS' : 'PEAQ (bez modyfikacji widma)'}) 
    ]

    dataFrame = results[  (results["filename"] == fileName) 
                        & (results["divider"] == "QMFWithHighbandModDivider") 
                        & (results["enhancer"] == "DummyEnhancer")
                        & (results["lowbandCompressor"] == "G7231Compressor")
                        & (results["highbandCompressor"] == "G7231Compressor")
                        & (results["highbandImpulseNumber"] == 4)
                        & (results["lowbandSeparateExcitation"].isnull())
                        & (results["highbandSeparateExcitation"].isnull())]
                        
    plotsData.append( 
        ResultsPlotData(
            dataFrame, 'lowbandImpulseNumber', ['PESQ', 'PEAQMOS'], 
            {'PESQ' : 'PESQ (odwrócenie widma\ngórnego pasma)', 'PEAQMOS' : 'PEAQ (odwrócenie widma\ngórnago pasma)'}
        ) 
    )

    plot = ResultsPlot(plotsData, '', 
                                    'figures/' + fileName + 'odDolnegoPasmaQmfMod.png', 'Liczba impulsów w dolnym paśmie', 'Aproksymacja MOS')
    plot.draw()


#################################################################################################################################################
#wykres zależności MOS od wzmocnienia górnego pasma

for fileName in fileNames:
    dataFrame = results[  (results["filename"] == fileName) 
                        & (results["divider"] == "QMFDivider") 
                        & (results["lowbandCompressor"] == "G7231Compressor")
                        & (results["lowbandImpulseNumber"] == 16)
                        & (results["highbandCompressor"] == "G7231Compressor")
                        & (results["highbandImpulseNumber"] == 8)
                        & (results["lowbandSeparateExcitation"].isnull())
                        & (results["highbandSeparateExcitation"].isnull())]

    plotsData = [ 
        ResultsPlotData
            (dataFrame, 'highbandEnhance', ['PESQ', 'PEAQMOS'], 
            {'PESQ' : 'PESQ', 'PEAQMOS' : 'PEAQ'}) 
    ]

    plot = ResultsPlot(plotsData, '',#'G723.1H_imp=8, G723.1L_imp=16,\nwsp. wzbudzenie, plik ' + fileName, 
                                    'figures/' + fileName + 'odWzmocnienia.png', 'wzmocnienie górnego pasma', 'Aproksymacja MOS')
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