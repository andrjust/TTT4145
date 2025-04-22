import matplotlib.pyplot as plt

def plotReceivedPackages(receivedPackages, length=1000):
    packages = list(range(length))
    received = [0]*length
    for pkg in receivedPackages:
        index = pkg[0]*256+pkg[1]
        if index < length:
            received[index] = 1

    # Plotting
    plt.figure(figsize=(12, 4))
    plt.plot(packages, received, label="1 m")
    plt.xlabel("Package Index")
    plt.ylabel("Received (1) / Not Received (0)")
    plt.title("Received Packages")
    plt.grid(True)
    plt.ylim(-0.2, 1.2)
    plt.tight_layout()
    plt.show()

def plotTotalBitError(wrongPackages, length=1000):
    packages = list(range(length))
    bitErrors = [0]*length
    totalError = 0
    for package in wrongPackages:
        totalError += package["wrongBits"]
        index = package["receive"][0:2]
        indexValue = index[0]*256+index[1]
        bitErrors[indexValue] = totalError
    
    for i in range(len(bitErrors)-1):
        if bitErrors[i] >= bitErrors[i+1]:
            bitErrors[i+1] = bitErrors[i]
    # Plotting
    plt.figure(figsize=(12, 4))
    plt.plot(packages, bitErrors, label="1 m")
    plt.xlabel("Package Index")
    plt.ylabel("Total Bit Errors")
    plt.title("Total Bit Errors")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return bitErrors