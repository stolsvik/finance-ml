"""
Splits the "WIKI_PRICES_xxxxxxxxxxxx.zip" files into separate files (with headers) based on the ticker.
"""

import zipfile
import os

dataPath = '/home/endre/Endre_finance_ml_data/'
splittedPath = dataPath + 'generated/WIKI_PRICES_SPLIT/'

os.makedirs(splittedPath, exist_ok=True)

wikiZip = zipfile.ZipFile(dataPath + 'WIKI_PRICES.zip', 'r')
f = wikiZip.open('WIKI_PRICES_212b326a081eacca455e13140d7bb9db.csv')
lines = 0
tickers = 0
header = f.readline()
print("Header:", header)

currentTicker = False
splitChar = ','.encode('ascii')
outputFile = 0
for line in f:
    lines += 1
    ticker = line.split(splitChar, 1)[0]
    if ticker != currentTicker:
        if outputFile != 0:
            outputFile.close()
        outputFile = open(splittedPath+ticker.decode('ascii')+'.csv', 'wb')
        currentTicker = ticker
        outputFile.write(header)
        print("Parsing Ticker", currentTicker)
    outputFile.write(line)

print("Number of lines:, ", lines)


