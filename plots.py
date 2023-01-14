import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

results = pd.read_csv('results.csv', encoding='cp1250', delimiter=';')

firstPlot = results[  (results["filename"] == "parole16.WAV") 
                    & (results["divider"] == "QMFDivider") 
                    & (results["enhancer"] == "DummyEnhancer")
                    & (results["lowbandCompressor"] == "G7231Compressor")
                    & (results["highbandCompressor"] == "G7231Compressor")
                    & (results["highbandImpulseNumber"] == 4)
                    & (results["lowbandSeparateExcitation"].isnull())
                    & (results["highbandSeparateExcitation"].isnull())]

#print(firstPlot.head())

# for i in firstPlot[:]:
#     print(i)

plt.plot(firstPlot['lowbandImpulseNumber'], firstPlot['PEAQ']+5, 'o-', label='PEAQ')
plt.plot(firstPlot['lowbandImpulseNumber'], firstPlot['PESQ'], 'o-', label='PESQ')
plt.grid(True)
plt.legend(title='Parameter where:')
#plt.show()
plt.savefig('figures/img1.svg',dpi=350)

plt.figure()
plt.plot(firstPlot['lowbandImpulseNumber'], firstPlot['PEAQ']-5, 'o-', label='PEAQ')
plt.plot(firstPlot['lowbandImpulseNumber'], firstPlot['PESQ']+8, 'o-', label='PESQ')
plt.grid(True)
plt.legend(title='Parameter where:')
#plt.show()
plt.savefig('figures/img2.svg',dpi=350)