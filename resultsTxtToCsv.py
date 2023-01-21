from parse import parse
import re
import csv

file = open('results.txt')
resultLines = file.readlines()
csvLines = []

def parseCompressorConfig(compressorConfigString):
    if re.match('.+Compressor.+', compressorConfigString):
        nameAndConfig = parse('{}Compressor{}', compressorConfigString).fixed
    elif re.match('.+Compressor', compressorConfigString):
        nameAndConfig = parse('{}Compressor', compressorConfigString).fixed
    else:
        raise ValueError(compressorConfigString)
    compressorName = nameAndConfig[0] + 'Compressor'
    impCount = str()
    sepExc = str()
    if len(nameAndConfig) > 1:
        if re.match('.+Imps.+', nameAndConfig[1]):
            config = parse('{}Imps{}',nameAndConfig[1]).fixed
        elif re.match('.+Imps', nameAndConfig[1]):
            config = parse('{}Imps',nameAndConfig[1]).fixed
        else:
            raise ValueError(compressorConfigString)
        impCount = config[0]
        if len(config) > 1:
            sepExc = config[1]
    return [compressorName, impCount, sepExc]

for resultLine in resultLines:
    parsed = []
    if re.match("DividingCompressor:\(divider:.*\)\(enhancer:.*\)\(bandCompressors:\[.*, .*\]\)\{'PEAQCompressionQualityMeasurer': '.*', 'PESQCompressionQualityMeasurer': '.*'\}\n", resultLine):
        parsedTuple = parse("DividingCompressor:(divider:{})(enhancer:{})(bandCompressors:[{}, {}]){'PEAQCompressionQualityMeasurer': '{}', 'PESQCompressionQualityMeasurer': '{}'}\n", resultLine).fixed
        parsed = list(parsedTuple)
    elif re.match("DividingCompressor:\(divider:.*\)\(enhancer:.*\)\(bandCompressors:\[.*, .*\]\).*\n", resultLine):
        parsedTuple = parse('DividingCompressor:(divider:{})(enhancer:{})(bandCompressors:[{}, {}])error\n', resultLine).fixed
        parsed = list(parsedTuple)
        parsed.append(-5)
        parsed.append(0)
    else:
        fileName = resultLine.replace('\n','')
    if len(parsed) > 0:
        divider = parsed[0]
        enhancer = parsed[1]
        lowbandCompressorConfig = parseCompressorConfig(parsed[2])
        highbandCompressorConfig = parseCompressorConfig(parsed[3])
        lowbandCompressor = lowbandCompressorConfig[0]
        lowbandImps = lowbandCompressorConfig[1]
        lowbandSepExc = lowbandCompressorConfig[2]
        highbandCompressor = highbandCompressorConfig[0]
        highbandImps = highbandCompressorConfig[1]
        highbandSepExc = highbandCompressorConfig[2]

        PEAQ = parsed[4]
        PESQ = parsed[5]
        csvLines.append([fileName, divider, enhancer, lowbandCompressor, lowbandImps, lowbandSepExc, highbandCompressor, highbandImps, highbandSepExc, PEAQ, PESQ])


header = ['filename','divider','enhancer','lowbandCompressor','lowbandImpulseNumber','lowbandSeparateExcitation','highbandCompressor','highbandImpulseNumber','highbandSeparateExcitation','PEAQ','PESQ']

with open('results_new.csv', 'w') as file:
    writer = csv.writer(file, delimiter=';',lineterminator='\n')
    writer.writerow(header)
    writer.writerows(csvLines)

print(csvLines)