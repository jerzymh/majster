from parse import parse
# patterns = {
#     'divider' : '\(divider:[A-Za-z]+\)',
#     'enhancer' : '\(enhancer:[A-Za-z\.0-9]+)',
#     'bandCompressors' : '\(bandCompressors:\[[A-Za-z0-9]+, [A-Za-z0-9]+\]\)',
#     'PEAQ' : '\'PEAQ.*,',
#     'PESQ' : '\'PESQ.*,'
# }

#file = open('results — kopia.txt')
#lines = file.readlines()

#line = "DividingCompressor:(divider:QMFDivider)(enhancer:DummyEnhancer)(bandCompressors:[G7231Compressor4Imps, G7231Compressor4Imps]){'PEAQCompressionQualityMeasurer': '-3.6456664140418673', 'PESQCompressionQualityMeasurer': '2.689'}\n"

line = "DividingCompressor:(divider:QMFDivider)(enhancer:DummyEnhancer)(bandCompressors:[G7231Compressor4Imps, G7231Compressor4Imps])\{'PEAQCompressionQualityMeasurer': '-3.6456664140418673', 'PESQCompressionQualityMeasurer': '2.689'}\n"
#parsed = parse("DividingCompressor:(divider:{})(enhancer:{})(bandCompressors:[{}, {}])\{'PEAQCompressionQualityMeasurer': '{}', 'PESQCompressionQualityMeasurer': '{}'\}\n", line)

parsed = parse("DividingCompressor:(divider:{})(enhancer:{})(bandCompressors:[{}, {}])\{'PEAQCompressionQualityMeasurer': '{}', 'PESQCompressionQualityMeasurer': '{}'}\n", line)

print(parsed)