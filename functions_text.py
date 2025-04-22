def extractBytes(file):
    text = ""

    with open(file, "rb") as f:
        text = f.read()
    text = list(text)
    return text

def makePackage(byteList, numBytesInPackage=256):
    packages = []
    for i in range(0, len(byteList), numBytesInPackage):
        if (i+numBytesInPackage <= len(byteList)):
            packages.append(byteList[i:i+numBytesInPackage])
    return packages

def analyzePackages(receivedPackages,transmitedPackages):
    local_receivedPackages = receivedPackages.copy()
    local_transmitedPackages = transmitedPackages.copy()

    lostPackages = 0
    correctPackages = 0
    wrongPackages = []
    indexErrors = 0

    # assume that the index of all received messages are correct!
    for receivedPackage in local_receivedPackages:
        index = receivedPackage[0:2]
        # simple check to see if index is wrong
        indexValue = index[0]*256+index[1]
        print(indexValue)
        if indexValue >= len(transmitedPackages):
            # byte error on the index!
            indexErrors += 1
            continue
        else:
            # assume correct index
            i = 0
            while i < (len(local_transmitedPackages)):
                if index != local_transmitedPackages[i][0:2]:
                    # assume this package is lost
                    local_transmitedPackages.pop(i)
                    lostPackages += 1
                else:
                    #check for byte errors
                    if local_transmitedPackages[i] == receivedPackage:
                        # assume no errors
                        correctPackages += 1
                        
                    else:
                        wrongBits = 0
                        for byteReceived, byteTransmitted in zip(receivedPackage, local_transmitedPackages[i]):
                            # find wrong bytes
                            if byteReceived != byteTransmitted:
                                # count number of wrong bits
                                binaryReceived = format(byteReceived, '08b')
                                binaryTransmitted = format(byteTransmitted, '08b')
                                for j in range(len(binaryReceived)):
                                    if binaryReceived[j] != binaryTransmitted[j]:
                                        wrongBits += 1
            
                        wrongPackage = {
                            "transmit" : local_transmitedPackages[i],
                            "receive" : receivedPackage,
                            "wrongBits" : wrongBits
                        }
                        wrongPackages.append(wrongPackage)
                    local_transmitedPackages.pop(i)
                    break
    return lostPackages, correctPackages, wrongPackages, indexErrors

#def analyzePackages(receivedPackages, transmitedPackages):
#    correctPackages = 0
#    wrongPackages = []
#    errorVsPackage = []
#    for i in range(len(receivedPackages)):
#        if receivedPackages[i] == transmitedPackages[i]:
#            correctPackages += 1
#            errorVsPackage.append([i,0])
#        else:
#            wrongBits = 0
#            for byteReceived, byteTransmitted in zip(receivedPackages[i], transmitedPackages[i]):
#                # find wrong bytes
#                if byteReceived != byteTransmitted:
#                    # count number of wrong bits
#                    binaryReceived = format(byteReceived, '08b')
#                    binaryTransmitted = format(byteTransmitted, '08b')
#                    for j in range(len(binaryReceived)):
#                        if binaryReceived[j] != binaryTransmitted[j]: wrongBits += 1
#
#            wrongPackage = {
#                "bytes" : receivedPackages[i],
#                "index" : i,
#                "wrongBits" : wrongBits
#            }
#            errorVsPackage.append([i,wrongBits])
#            wrongPackages.append(wrongPackage)
#    return correctPackages, wrongPackages, errorVsPackage