import matplotlib.pyplot as plt

from functions_text import extractBytes
from functions_text import makePackage
from functions_text import analyzePackages

from plot_text import plotReceivedPackages
from plot_text import plotTotalBitError

transmitBytes = extractBytes("TransmitText.txt")
transmitPackages = makePackage(transmitBytes)
receivedBytes = extractBytes("ReceivedText.txt")
receivedBytes = receivedBytes[1:] # remove the first one?
receivedPackages = makePackage(receivedBytes)

#correctPackages, wrongPackages, errorVsPackage = analyzePackages(receivedPackages, transmitPackages)
lostPackages, correctPackages, wrongPackages, indexErrors = analyzePackages(receivedPackages, transmitPackages)

print(lostPackages)
print(correctPackages)
print(len(wrongPackages))
plotReceivedPackages(receivedPackages)
plotTotalBitError(wrongPackages)