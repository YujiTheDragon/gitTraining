import psutil

def DisplayRAM_Usage():
    getUsedVirtualMemory = psutil.virtual_memory()[3]/1000000000
    getAvailVirtualMemory = psutil.virtual_memory()[4]/1000000000

    print ("RAM memory used: ",str(psutil.virtual_memory()[2])+"%")
    print (f"RAM Used (GB): {getUsedVirtualMemory:.2f}GB")
    print (f"RAM Available (GB): {getAvailVirtualMemory:.2f}GB")

def RamTest(testRange):
    for i in range(testRange):
        RamTest(testRange-1)
